from flask import Flask, render_template, request, send_file
import pandas as pd  # Assuming you're working with CSV/Excel files
import io
from openpyxl import load_workbook

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file1' not in request.files or 'file2' not in request.files:
            return redirect(request.url)

        file1 = request.files['file1']
        file2 = request.files['file2']

        if file1.filename == '' or file2.filename == '':
            return redirect(request.url)

        if file1 and file2:
            output_buffer = merge_files(file1, file2)

            # Return the buffer as a downloadable file
            return send_file(output_buffer, as_attachment=True, download_name='merged_file.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    return render_template('index.html')

def merge_files(file1, file2):
    # Read the files into DataFrames
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Create a pivot table from df1
    pivot_table = pd.pivot_table(df1, index=['Segment', 'Sub Division', 'Report List'],
                             values=['Delivered', 'Open', 'Clicks', 'Unsubscibes', 'Complaints'],
                             aggfunc='sum', fill_value=0)

    # Create a BytesIO buffer
    buffer = io.BytesIO()

    # Save the pivot table to the buffer
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        pivot_table.to_excel(writer, sheet_name='PivotTable', index=True)

    # Ensure the buffer is at the beginning
    buffer.seek(0)

    # Load sheet1 for merging
    wb = load_workbook('sheet1.xlsx')
    ws = wb.active

    # Convert the sheet1 data to a pandas DataFrame
    sheet1_df = pd.DataFrame(ws.values)
    sheet1_df.columns = sheet1_df.iloc[0]
    sheet1_df = sheet1_df[1:]

    # Load the pivot table data from the buffer
    buffer.seek(0)
    pivot_df = pd.read_excel(buffer, sheet_name='PivotTable')

    # Ensure relevant columns are properly named
    pivot_df = pivot_df[['Report List', 'Delivered', 'Open', 'Clicks', 'Unsubscibes', 'Complaints']]

    # Update sheet1 values with the pivot table values
    for index, row in sheet1_df.iterrows():
        matching_row = pivot_df[pivot_df['Report List'] == row['Report List']]
        if not matching_row.empty:
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Delivered') + 1).value = matching_row['Delivered'].values[0]
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Open') + 1).value = matching_row['Open'].values[0]
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Clicks') + 1).value = matching_row['Clicks'].values[0]
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Unsubscibes') + 1).value = matching_row['Unsubscibes'].values[0]
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Complaints') + 1).value = matching_row['Complaints'].values[0]

    # Process df2 to add List_id
    df2['Source (Sub Publisher)'] = df2['Source (Sub Publisher)'].astype(str)
    df2['List_id'] = df2['Source (Sub Publisher)'].apply(lambda x: int(x.split('_')[-1]) if (x.split('_')[-1]).isdigit() else x.split('_')[-1] )

    # Rearrange columns to place List_id next to Source (Sub Publisher)
    columns = list(df2.columns)
    source_index = columns.index('Source (Sub Publisher)')
    columns.insert(source_index + 1, columns.pop(-1))
    df2 = df2[columns]

    # Group df2 by List_id
    df2_grouped = df2.groupby('List_id').agg({'Unique Clicks': 'sum', 'Gross Clicks': 'sum', 'Payout': 'sum'}).reset_index()

    # Convert grouped data to dictionary
    sheet2_dict = df2_grouped.set_index('List_id').to_dict(orient='index')

    # Update sheet1 with values from df2_grouped
    for index, row in sheet1_df.iterrows():
        list_id = row['List_id']
        if list_id in sheet2_dict:
            data = sheet2_dict[list_id]
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Unique Clicks') + 1).value = data['Unique Clicks']
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Gross Clicks') + 1).value = data['Gross Clicks']
            ws.cell(row=index + 1, column=sheet1_df.columns.get_loc('Payout') + 1).value = data['Payout']

    # Save the updated workbook to the buffer
    buffer.seek(0)
    wb.save(buffer)
    buffer.seek(0)

    return buffer

if __name__ == '__main__':
    app.run(debug=True)

let file1Uploaded = false;
let file2Uploaded = false;

function updateStatus() {
    const statusLine1 = document.getElementById('statusLine1');
    const statusLine2 = document.getElementById('statusLine2');
    const statusCircle = document.getElementById('statusCircle');
    const downloadBtn = document.getElementById('downloadBtn');
    const pross = document.getElementById('text')

    if (document.getElementById('fileInput1').files.length > 0) {
        file1Uploaded = true;
        statusLine1.style.backgroundColor = '#28a745';
    }

    if (document.getElementById('fileInput2').files.length > 0) {
        file2Uploaded = true;
    }

    if (file1Uploaded && file2Uploaded) {
        statusCircle.style.backgroundColor = '#FFB318';
        pross.style.color = '#FFFFFF';
        pross.innerHTML = 'DONE';
        statusLine2.style.backgroundColor = '#28a745';
        downloadBtn.disabled = false;
        alert('Both files uploaded successfully! Ready to merge and download.');
    }
}

document.getElementById('fileInput1').addEventListener('change', updateStatus);
document.getElementById('fileInput2').addEventListener('change', updateStatus);

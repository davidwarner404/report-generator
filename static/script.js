let file1Uploaded = false;
let file2Uploaded = false;
let file3Uploaded = false;
let file4Uploaded = false;

document.getElementById('EM01').classList.add('active');
function openTab(event, tabId) {
    // Remove active class from all tabs and buttons
    const tabContents = document.querySelectorAll('.tab-content');
    const tabButtons = document.querySelectorAll('.tab-button');
    
    tabContents.forEach(tab => tab.classList.remove('active'));
    tabButtons.forEach(button => button.classList.remove('active'));

    // Add active class to the selected tab and button
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
}


function updateStatus() {
    const statusLine1 = document.getElementById('statusLine1');
    const statusLine2 = document.getElementById('statusLine2');
    const statusCircle1 = document.getElementById('statusCircle1');
    const downloadBtn01 = document.getElementById('downloadBtn01');
    const pross = document.getElementById('text1')

    if (document.getElementById('fileInput1').files.length > 0) {
        file1Uploaded = true;
        statusLine1.style.backgroundColor = '#28a745';
    }

    if (document.getElementById('fileInput2').files.length > 0) {
        file2Uploaded = true;
    }

    if (file1Uploaded && file2Uploaded) {
        statusCircle1.style.backgroundColor = '#FFB318';
        pross.style.color = '#FFFFFF';
        pross.innerHTML = 'DONE';
        statusLine2.style.backgroundColor = '#28a745';
        downloadBtn01.disabled = false;
        alert('Both files uploaded successfully! Ready to merge and download.');
    }
}

document.getElementById('fileInput1').addEventListener('change', updateStatus);
document.getElementById('fileInput2').addEventListener('change', updateStatus);


function updateStatus2() {
    const statusLine3 = document.getElementById('statusLine3');
    const statusLine4 = document.getElementById('statusLine4');
    const statusCircle2 = document.getElementById('statusCircle2');
    const downloadBtn02 = document.getElementById('downloadBtn02');
    const pross = document.getElementById('text2')

    if (document.getElementById('fileInput3').files.length > 0) {
        file3Uploaded = true;
        statusLine3.style.backgroundColor = '#28a745';
    }

    if (document.getElementById('fileInput4').files.length > 0) {
        file4Uploaded = true;
    }

    if (file3Uploaded && file4Uploaded) {
        statusCircle2.style.backgroundColor = '#FFB318';
        pross.style.color = '#FFFFFF';
        pross.innerHTML = 'DONE';
        statusLine4.style.backgroundColor = '#28a745';
        downloadBtn02.disabled = false;
        alert('Both files uploaded successfully! Ready to merge and download.');
    }
}

document.getElementById('fileInput3').addEventListener('change', updateStatus2);
document.getElementById('fileInput4').addEventListener('change', updateStatus2);

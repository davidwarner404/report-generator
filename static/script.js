let file1Uploaded = false;
let file2Uploaded = false;

function uploadFile() {
    const circuit1 = document.getElementById('circuit1');
    const circuit3 = document.getElementById('circuit3');
    const mergePoint = document.getElementById('mergePoint');
    const downloadBtn = document.getElementById('downloadBtn');

    if (document.getElementById('fileInput1').files.length > 0) {
        file1Uploaded = true;
        circuit1.classList.add('active');
    }

    if (document.getElementById('fileInput2').files.length > 0) {
        file2Uploaded = true;
    }

    if (file1Uploaded && file2Uploaded) {
        mergePoint.classList.add('active');
        circuit3.classList.add('active');
        downloadBtn.disabled = false;

        // Show success alert
        alert('Both files uploaded successfully! Ready to merge and download.');
    }
}

document.getElementById('fileInput1').addEventListener('change', uploadFile);
document.getElementById('fileInput2').addEventListener('change', uploadFile);

function uploadImage() {
    const form = document.getElementById('uploadForm');
    const uploadedImage = document.getElementById('uploadedImage');
    const resultSection = document.getElementById('resultSection');

    // Check if a file is selected
    if (form.image.files.length === 0) {
        alert('Please select an image.');
        return;
    }

    const formData = new FormData(form);

    // Display the uploaded image
    const reader = new FileReader();
    reader.onload = function (e) {
        uploadedImage.src = e.target.result;
        uploadedImage.style.display = 'block';
    };
    reader.readAsDataURL(form.image.files[0]);

    // Send image to the server for processing
    fetch('/uploads', {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(result => {
            // Display the results
            resultSection.innerHTML = `<p>Result: ${result}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultSection.innerHTML = '<p>An error occurred during processing.</p>';
        });
}

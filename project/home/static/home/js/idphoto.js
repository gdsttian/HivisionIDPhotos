document.getElementById("imageInput").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        // Preview the image locally
        const reader = new FileReader();
        reader.onload = function(e) {
            const imagePreview = document.getElementById("imagePreview");
            imagePreview.src = e.target.result;
            imagePreview.style.display = "block";
        };
        reader.readAsDataURL(file);
    }
});

// Upload image to the server (just an example)
function uploadImage() {
    const fileInput = document.getElementById("imageInput");
    const file = fileInput.files[0];
    
    if (!file) {
        alert("Please select an image to upload.");
        return;
    }
    
    const formData = new FormData();
    formData.append("image", file);

    // Example: Send the image to the server using fetch (or another method)
    fetch("/upload-endpoint", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log("Image uploaded successfully", data);
        alert("Image uploaded successfully!");
    })
    .catch(error => {
        console.error("Error uploading image:", error);
        alert("Failed to upload image.");
    });
}


// Initialize the webcam
async function initializeWebcam() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        document.getElementById('webcam').srcObject = stream;
    } catch (err) {
        console.error('Error accessing webcam: ', err);
        alert('Could not access webcam');
    }
}

// Capture an image from the webcam
function captureImage() {
    const video = document.getElementById('webcam');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    
    // Set the canvas dimensions to match the video feed
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Draw the current video frame onto the canvas
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Get the data URL of the canvas image
    const dataUrl = canvas.toDataURL('image/png');

    // Display the captured image
    const capturedImage = document.getElementById('capturedImage');
    capturedImage.src = dataUrl;
    capturedImage.style.display = 'block';  // Show the image
}

// Initialize the webcam on page load
window.onload = initializeWebcam;

// Enable the paste event when the user clicks the button
function enablePaste() {
    // Inform the user to paste an image from the clipboard
    alert("Now paste an image from the clipboard using Ctrl+V (or Cmd+V on Mac).");
    
    // Listen for the paste event on the document
    document.addEventListener("paste", handlePaste);
}

// Handle the paste event
async function handlePaste(event) {
    // Prevent the default paste behavior (which might be text)
    event.preventDefault();

    // Check if the clipboard contains items (images or other media)
    const items = event.clipboardData.items;

    for (let i = 0; i < items.length; i++) {
        const item = items[i];

        // Check if the item is of type image
        if (item.type.indexOf("image") === 0) {
            // Get the image file from the clipboard
            const file = item.getAsFile();
            
            // Create an object URL for the image
            const imgURL = URL.createObjectURL(file);
            
            // Display the image in the image preview element
            const imagePreview = document.getElementById("imagePreview");
            imagePreview.src = imgURL;
            imagePreview.style.display = "block"; // Show the image
            
            break; // Only handle the first image in the clipboard
        }
    }
}

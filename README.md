# Face Verification 
This project implements a web service API for facial feature similarity verification between two uploaded images. The API is built using Flask, a lightweight web framework for Python, and OpenCV, a popular library for computer vision tasks.

### Functionalities

- Accepts image uploads through a POST request.
- Performs facial detection on each uploaded image using Haar cascade classifiers.
- Extracts keypoints and descriptors from detected faces using the Scale-Invariant Feature Transform (SIFT) algorithm.
- Matches keypoint descriptors between the two images to identify potential similarities.
- Applies a ratio test to filter out weak matches and ensure robustness.
- Returns a JSON response indicating whether significant similarity in facial features is detected between the uploaded images.

### Usage

1. **Prerequisites:**
   - Python 3.x
   - Flask
   - OpenCV
   - NumPy
2. **Running the API:**
   - Clone this repository.
   - Install required dependencies using `pip install -r requirements.txt`.
   - Run the Flask development server using `python app.py`.
   - Access the API endpoint at `http://127.0.0.1:5000/` (default port).

3. **Testing the API:**
   - Use a tool like Postman or curl to send a POST request to the API endpoint with two image files included in the request body using multipart/form-data encoding.
   - The request body should include two key-value pairs:
     - `image1`: The first image file for comparison.
     - `image2`: The second image file for comparison.
   - The API will respond with a JSON object containing a key named either:
     - `result`: with a message indicating the outcome (e.g., "Similarity in facial features detected").
     - `error`: with an error message in case of any exceptions during processing.


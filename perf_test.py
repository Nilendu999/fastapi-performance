# import os
# from locust import HttpUser, task, between

# class MyUser(HttpUser):
#     wait_time = between(1, 5)  # Random wait time between 1 and 5 seconds

#     @task
#     def upload_pdf(self):
#         # Replace the URL with the actual URL of your FastAPI server
#         url = "http://localhost:8000/upload/"
#         headers = {
#             "Content-Type": "multipart/form-data",
#         }

#         # Provide the absolute path to the PDF file for testing
#         pdf_file_path = r"C:\home\dev\perf\data\00 IAS Syllabus for Prelims and Mains by UPSC.pdf"

#         # Ensure the PDF file exists
#         if not os.path.exists(pdf_file_path):
#             print(f"PDF file not found: {pdf_file_path}")
#             return

#         # Specify the response_type parameter
#         response_type = "json"

#         # Create a dictionary with the file data
#         files = {"file": (os.path.basename(pdf_file_path), open(pdf_file_path, "rb"))}

#         # Send the POST request
#         self.client.post(url, files=files, data={"response_type": response_type}, headers=headers)

import os
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Random wait time between 1 and 5 seconds

    @task
    def upload_pdf(self):
        # Replace the URL with the actual URL of your FastAPI server
        url = "http://localhost:8000/upload/"

        # Provide the absolute path to the PDF file for testing
        pdf_file_path = r"C:\home\dev\perf\data\00 IAS Syllabus for Prelims and Mains by UPSC.pdf"

        # Ensure the PDF file exists
        if not os.path.exists(pdf_file_path):
            print(f"PDF file not found: {pdf_file_path}")
            return

        # Create a dictionary for the files data
        files = {
            'file': (os.path.basename(pdf_file_path), open(pdf_file_path, 'rb'), 'application/pdf')
        }

        # Specify the response_type parameter
        response_type = "json"

        # Send the POST request with the PDF file and response_type parameter
        response = self.client.post(url, data={"response_type": response_type}, files=files)

        # You can add assertions or log response data here if needed
        # For example: assert response.status_code == 200
        
        # Validate the response
        assert response.status_code == 200, f"Received unexpected status code: {response.status_code}"
        response_data = response.json()

        # Perform JSON response validation
        assert "filename" in response_data, "Response does not contain 'filename' field"
        assert "page_count" in response_data, "Response does not contain 'page_count' field"
        
        # You can add more specific validation checks here as needed

        # Optionally, log response data
        print(f"Response Data: {response_data}")


# Backend API for AI Notes

**API Base URL:** `https://ai-notes-backend.onrender.com`

This backend service processes user-submitted images containing mathematical expressions or conceptual queries and leverages the Gemini Large Language Model (LLM) for interpretation and solution generation.

**Important Note (Cold Start):**  This API is deployed on a free instance and may experience a cold start of 50 seconds or more.  Please be patient when initially accessing the API or sending the first request after a period of inactivity.

## Endpoints

### 1. GET `/` - Welcome Message

*   **Path:** `/`
*   **Description:**  Returns a simple JSON response containing a welcome message, API version, and a link to the documentation.
*   **Method:** `GET`
*   **Request Body:** None
*   **Example Response:**

    ```json
    {
      "message": "Welcome to my API!\n",
      "version": "1.0.0",
      "docs": "/docs"
    }
    ```

### 2. POST `/calculate` - Image Processing and Calculation

*   **Path:** `/calculate`
*   **Description:**  Receives a base64-encoded image and an optional dictionary of user-defined variables.  The Gemini LLM analyzes the image to identify and solve mathematical expressions. It can also utilize the provided variables in its calculations.
*   **Method:** `POST`
*   **Request Body:**  `ImageData` (see schema below)
*   **Request Body Schema (`ImageData`):**

    ```json
    {
      "image": "data:image/png;base64,<encoded_data>",
      "dict_of_vars": {
        "x": 2,
        "y": 3
      }
    }
    ```

    *   `image`:  **Required.**  A base64-encoded string representing the image.  The string *must* include the data URI prefix (e.g., `data:image/png;base64,`).  Supported image formats depend on what the Gemini LLM accepts (likely PNG, JPEG, etc.).
    *   `dict_of_vars`: **Optional.** A dictionary where keys are variable names (strings) and values are their corresponding numerical values. These variables can be referenced within the mathematical expressions in the image.

*   **Example Successful Response:**

    ```json
    {
      "message": "Image processed",
      "result": [
        {
          "expr": "x",
          "result": "2",
          "assign": true
        }
      ],
      "status": "success"
    }
    ```
    * `message`: A general status message.
    *   `result`: An array of objects.  Each object represents a solved expression or assigned variable:
        *   `expr`: The mathematical expression or variable name found in the image.
        *   `result`: The calculated result of the expression, or the value assigned to the variable.
        *   `assign`:  A boolean indicating whether this entry represents a variable assignment (`true`) or a calculated expression (`false`).
    * `status`: Indicates the overall success or failure of the operation.

*   **Example Error Response** (Possible, but structure might vary):
    *   If the image is invalid, the Gemini model fails, or other problems:

        ```json
        {
            "message": "Error processing image",
            "error": "Invalid image format", // or a more specific error message
            "status": "error"
        }
        ```
        ```json
        {
            "message": "Error processing image",
            "error": "Internal Server error. Gemini API error", // or a more specific error message
            "status": "error"
        }
        ```
        ```json
         {
            "message": "Error processing image",
            "error": "No mathematical expressions found",
            "status": "error"
        }
        ```

## Notes

*   **Error Handling:** The provided example responses show a basic structure for success and error scenarios.  The actual error messages and structure might vary depending on the specific error encountered.  Robust error handling should be implemented in any client application consuming this API.
* **Image format**: The base64 encoded string must be a valid base64 representation of an image, including the data URI prefix.
* **Gemini LLM limitations**: The capacity of recognizing the expressions depends on the Gemini LLM used.
* **Variable names**: Ensure the names in the `dict_of_vars` match the variables present in the image.

This revised version is much more suitable for a `README.md` file. It's clearly organized, uses Markdown formatting effectively, and provides all the necessary details for a developer to understand and use the API. I've also added error response examples and important considerations.
import logo from "./logo.svg";
import "./App.css";
import { useState } from "react";
import { useDropzone } from "react-dropzone";
import { ArrowUpOnSquareIcon } from "@heroicons/react/24/outline"; // assuming you have Heroicons installed
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const DragAndDropPDFUploader = () => {
  const [file, setFile] = useState(null);

  const [uploading, setUploading] = useState(false);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: "application/pdf",
    multiple: false,
    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        if (acceptedFiles[0].type === "application/pdf") {
          setFile(acceptedFiles[0]);
        } else {
          toast.error("You can only upload PDF files");
        }
      }
    },
  });

  const handleUpload = () => {
    if (file) {
      setUploading(true);
      const formData = new FormData();
      formData.append("file", file);
      fetch(`${process.env.REACT_APP_BACKEND_URL}/parse-pdf`, {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (response.ok) {
            toast.success("File uploaded successfully");
            // log the json response
            response.json().then((data) => {
              console.log(data.filename);
            });
          } else {
            toast.error("Something went wrong");
          }
          setUploading(false);
        })
        .catch((error) => {
          console.error(error);
          toast.error("Something went wrong");
          setUploading(false);
        });
    }
  };
  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <div
        {...getRootProps()}
        className="w-200 h-56 border-2 border-gray-800 rounded-lg px-4 py-8 flex flex-col items-center justify-center cursor-pointer hover:bg-gray-100"
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <p className="text-2xl text-gray-600">Drop the PDF here</p>
        ) : (
          <div className="flex flex-col items-center justify-center">
            <ArrowUpOnSquareIcon className="h-12 w-12 text-gray-600" />
            <p className="text-lg text-gray-600 mt-2">
              Drag and drop a PDF file here or click to select a file
            </p>
          </div>
        )}
      </div>
      {file && (
        <div className="mt-8">
          <p className="text-xl text-gray-600">Selected file:</p>
          <p className="text-lg font-medium">{file.name}</p>
          <button
            onClick={handleUpload}
            className="mt-4 bg-gradient-to-r from-blue-400 to-indigo-500 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out hover:bg-gradient-to-r hover:from-indigo-500 hover:to-blue-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 disabled:opacity-50 disabled:cursor-not-allowed"
            disabled={uploading}
          >
            {uploading ? "Uploading..." : "Upload"}
          </button>
        </div>
      )}
      <ToastContainer />
    </div>
  );
};

// export default DragAndDropPDFUploader;

function App() {
  return (
    <div className="App">
      <DragAndDropPDFUploader />
    </div>
  );
}

export default App;

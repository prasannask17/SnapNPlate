// import React, { useState, useEffect } from "react";
// import axios from "axios";

// function ImageUpload({ setData, setErr }) {
//   const [selectedFile, setSelectedFile] = useState(null);
//   const [image, setImage] = useState(false);
//   const [isLoading, setIsLoading] = useState(false);
//   const threshold = 0.5;

//   const sendFile = async () => {
//     if (image) {
//       let formData = new FormData();
//       formData.append("file", selectedFile);
//       try {
//         let res = await axios.post(process.env.REACT_APP_API_URL, formData);
//         if (res.status === 200) {
//           console.log(res.data);
//           if (res.data.confidence < threshold) {
//             setData({ class: "Default", confidence: "100" });
//             clearData();
//             setErr(true);
//           } else {
//             setData(res.data);
//           }
//         }
//       } catch (error) {
//         console.error("Error uploading file:", error);
//       }
//       setIsLoading(false);
//     }
//   };

//   const clearData = () => {
//     setData({ class: "Default", confidence: "100" });
//     setImage(false);
//     setSelectedFile(null);
//   };

//   const onSelectFile = (event) => {
//     const file = event.target.files[0];
//     if (!file) {
//       clearData();
//       return;
//     }
//     setSelectedFile(file);
//     setImage(true);
//   };

//   useEffect(() => {
//     if (!selectedFile) {
//       return;
//     }
//     setIsLoading(true);
//     setErr(false);
//     sendFile();
//   }, [selectedFile]);

//   return (
//     <>
//       <div className="col-12 col-sm-3 ">
//         <div class="input-group mb-3 ps-3 ">
//           <input
//             type="file"
//             class="form-control"
//             accept="image/*"
//             onChange={onSelectFile}
//             id="imageInput"
//           />
//           <label class="input-group-text">Upload</label>
//         </div>
//       </div>

//       {isLoading && <p>Loading...</p>}
//       <div className="col-12 col-sm-2">
//         <button className="btn btn-dark" onClick={clearData}>
//           Clear
//         </button>
//       </div>
//     </>
//   );
// }

// export default ImageUpload;

import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

function ImageUpload({ setData, setErr }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [image, setImage] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [preview, setPreview] = useState(null);
  const fileInputRef = useRef(null);
  const threshold = 0.5;

  const sendFile = async () => {
    if (image) {
      let formData = new FormData();
      formData.append("file", selectedFile);
      try {
        let res = await axios.post(process.env.REACT_APP_API_URL, formData);
        if (res.status === 200) {
          console.log(res.data);
          if (res.data.confidence < threshold) {
            setData({ class: "Default", confidence: "100" });
            clearData();
            setErr(true);
          } else {
            setData(res.data);
          }
        }
      } catch (error) {
        console.error("Error uploading file:", error);
      }
      setIsLoading(false);
    }
  };

  const clearData = () => {
    setData({ class: "Default", confidence: "100" });
    setImage(false);
    setSelectedFile(null);
    setPreview(null);
    // Reset the file input so filename clears
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const onSelectFile = (event) => {
    const file = event.target.files[0];
    if (!file) {
      clearData();
      return;
    }
    setSelectedFile(file);
    setImage(true);
    setPreview(URL.createObjectURL(file));
  };

  useEffect(() => {
    if (!selectedFile) {
      return;
    }
    setIsLoading(true);
    setErr(false);
    sendFile();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedFile]);

  return (
    <>
      <div className="col-12 col-sm-3">
        <div className="input-group mb-3 ps-3">
          <input
            type="file"
            className="form-control"
            accept="image/*"
            onChange={onSelectFile}
            ref={fileInputRef}
            id="imageInput"
          />
          <label className="input-group-text">Upload</label>
        </div>
      </div>

      {isLoading && <p>Loading...</p>}

      {preview && (
        <div className="col-12 ps-3 pb-3">
          <img
            src={preview}
            alt="Uploaded preview"
            style={{ maxHeight: "200px", borderRadius: "8px" }}
          />
        </div>
      )}

      <div className="col-12 col-sm-2">
        <button className="btn btn-dark" onClick={clearData}>
          Clear
        </button>
      </div>
    </>
  );
}

export default ImageUpload;

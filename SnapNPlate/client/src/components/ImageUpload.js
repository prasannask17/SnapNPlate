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

import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";

function ImageUpload({ setData, setErr }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [image, setImage] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const threshold = 0.5;

  const clearData = useCallback(() => {
    setData({ class: "Default", confidence: "100" });
    setImage(false);
    setSelectedFile(null);
  }, [setData]);

  // Wrapped in useCallback to satisfy dependency rules
  const sendFile = useCallback(async () => {
    if (image && selectedFile) {
      let formData = new FormData();
      formData.append("file", selectedFile);
      try {
        let res = await axios.post(process.env.REACT_APP_API_URL, formData);
        if (res.status === 200) {
          if (res.data.confidence < threshold) {
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
  }, [image, selectedFile, setData, setErr, clearData]);

  const onSelectFile = (event) => {
    const file = event.target.files[0];
    if (!file) {
      clearData();
      return;
    }
    setSelectedFile(file);
    setImage(true);
  };

  useEffect(() => {
    if (!selectedFile) {
      return;
    }
    setIsLoading(true);
    setErr(false);
    sendFile();
    
    // Dependencies are now correctly tracked
  }, [selectedFile, sendFile, setErr]);

  return (
    <div className="upload-section">
      <div className="upload-controls">
        <input
          type="file"
          className="form-control"
          accept="image/*"
          onChange={onSelectFile}
          id="imageInput"
        />
      </div>

      {isLoading && <p className="loading-text">Analyzing ingredients...</p>}
      
      <button className="btn-clear" onClick={clearData}>
        Clear Selection
      </button>
    </div>
  );
}

export default ImageUpload;

// import React, { useState, useEffect, useRef } from "react";
// import axios from "axios";
// import "../App.css";

// function ImageUpload({ setData, setErr }) {
//   const [selectedFile, setSelectedFile] = useState(null);
//   const [image, setImage] = useState(false);
//   const [isLoading, setIsLoading] = useState(false);
//   const [preview, setPreview] = useState(null);
//   const fileInputRef = useRef(null);
//   const threshold = 0.5;

//   const sendFile = async () => {
//     if (image) {
//       let formData = new FormData();
//       formData.append("file", selectedFile);
//       try {
//         let res = await axios.post(process.env.REACT_APP_API_URL, formData);
//         if (res.status === 200) {
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
//     setPreview(null);
//     if (fileInputRef.current) fileInputRef.current.value = "";
//   };

//   const onSelectFile = (event) => {
//     const file = event.target.files[0];
//     if (!file) { clearData(); return; }
//     setSelectedFile(file);
//     setImage(true);
//     setPreview(URL.createObjectURL(file));
//   };

//   useEffect(() => {
//     if (!selectedFile) return;
//     setIsLoading(true);
//     setErr(false);
//     sendFile();
//   // eslint-disable-next-line react-hooks/exhaustive-deps
//   }, [selectedFile]);

//   return (
//     <>
//       <div style={{display:"flex", alignItems:"center", gap:"12px", flexWrap:"wrap"}}>
//         <input
//           type="file"
//           className="form-control"
//           accept="image/*"
//           onChange={onSelectFile}
//           ref={fileInputRef}
//           style={{maxWidth:"280px", borderRadius:"8px", fontSize:"0.9rem"}}
//         />
//         {isLoading && <span className="loading-text">Identifying food...</span>}
//         <button className="btn-clear" onClick={clearData}>Clear</button>
//       </div>
//       {preview && (
//         <img src={preview} alt="Uploaded preview" className="uploaded-preview" style={{marginTop:"12px"}} />
//       )}
//     </>
//   );
// }

// export default ImageUpload;

import React from "react";
import "../styles.css";

function Instructions({ instructions }) {
  return (
    <div className="text-start ps-3 mb-5">
      <h1>Instructions</h1>
      <ul class="list-group list-group-flush ps-5">
        {instructions.map((instruction, ind) => (
          <li className="list-group-item" key={ind}>
            {ind + 1}. {instruction}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Instructions;

// import React from "react";
// import "../App.css";

// function Instructions({ instructions }) {
//   return (
//     <div className="detail-section">
//       <h2 className="detail-title">Instructions</h2>
//       <ul className="detail-list">
//         {instructions.map((instruction, ind) => (
//           <li key={ind}>{ind + 1}. {instruction}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default Instructions;

import React from "react";
import "../styles.css";

function Ingredients({ ingredients }) {
  return (
    <div className="text-start ps-3 mb-5">
      <h1>Ingredients</h1>
      <ul class="list-group list-group-flush ps-5">
        {ingredients.map((ingredient, ind) => (
          <li className="list-group-item" key={ind}>
            {`${ind + 1}. ${ingredient["name"]} - ${ingredient["qty"]}`}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Ingredients;

// import React from "react";
// import "../App.css";

// function Ingredients({ ingredients }) {
//   return (
//     <div className="detail-section">
//       <h2 className="detail-title">Ingredients</h2>
//       <ul className="detail-list">
//         {ingredients.map((ingredient, ind) => (
//           <li key={ind}>{ind + 1}. {ingredient["name"]} — {ingredient["qty"]}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default Ingredients;

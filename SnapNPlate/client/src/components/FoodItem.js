// import React from "react";
// import "../styles.css";

// function FoodItem({
//   name,
//   description,
//   nutrientFacts,
//   veg,
//   prepTime,
//   cookingTime,
//   serving,
// }) {
//   const imgPath = `/assets/foodImages/${name}.jpg`;
//   return (
//     <>
//       <div className="col-12 col-sm-6 p-5">
//         <img src={imgPath} class="img-fluid food-pic rounded" alt="..." />
//       </div>
//       <div className="col-12 col-sm-6 p-5">
//         <div className="text-start">
//           <h1>{name !== "Default" ? name : "Your Next Meal"}</h1>
//         </div>
//         <p className="fs-4">{description}</p>
//         <div class="row align-items-center pt-5">
//           <div class="col-6 col-xl-3">
//             <img
//               className="icon"
//               src="/assets/icons/preparationTime-icon.svg"
//               alt=""
//             />
//             <span>{prepTime}</span>
//           </div>
//           <div class="col-6 col-xl-3 ps-3">
//             <img
//               className="icon"
//               src="/assets/icons/cookingTime-icon.svg"
//               alt=""
//             />
//             <span>{cookingTime}</span>
//           </div>
//           <div class="col-6 col-xl-3">
//             <img
//               className="icon"
//               src="/assets/icons/servings-icon.svg"
//               alt=""
//             />
//             <span>{serving}</span>
//           </div>
//           <div class="col-6 col-xl-3 pe-5">
//             {veg ? (
//               <img className="icon" src="/assets/icons/veg-icon.svg" alt="" />
//             ) : (
//               <img
//                 className="icon"
//                 src="/assets/icons/nonveg-icon.svg"
//                 alt=""
//               />
//             )}
//           </div>
//         </div>
//         <div className="text-start p-3">
//           <h1>Nutrition Facts</h1>
//           <table class="table table-dark table-striped">
//             <tbody>
//               <tr>
//                 <th scope="row">Fat</th>
//                 <td>{nutrientFacts["fat"]}</td>
//               </tr>
//               <tr>
//                 <th scope="row">Protein</th>
//                 <td>{nutrientFacts["protein"]}</td>
//               </tr>
//               <tr>
//                 <th scope="row">Sugar</th>
//                 <td colSpan="2">{nutrientFacts["sugar"]}</td>
//               </tr>
//               <tr>
//                 <th scope="row">Carbs</th>
//                 <td colSpan="2">{nutrientFacts["carbo"]}</td>
//               </tr>
//             </tbody>
//           </table>
//         </div>
//       </div>
//     </>
//   );
// }

// export default FoodItem;

// import React from "react";
// import "../styles.css";

// function FoodItem({
//   name,
//   description,
//   nutrientFacts,
//   veg,
//   prepTime,
//   cookingTime,
//   serving,
// }) {
//   const pngFoods = ["Kulfi", "Samosa"];
//   const ext = pngFoods.includes(name) ? "png" : "jpg";
//   const imgPath = `/assets/foodImages/${name}.${ext}`;
//   return (
//     <>
//       <div className="col-12 col-sm-6 p-5">
//         <img src={imgPath} class="img-fluid food-pic rounded" alt="..." />
//       </div>
//       <div className="col-12 col-sm-6 p-5">
//         <div className="text-start">
//           <h1>{name !== "Default" ? name : "Your Next Meal"}</h1>
//         </div>
//         <p className="fs-4">{description}</p>
//         <div class="row align-items-center pt-5">
//           <div class="col-6 col-xl-3">
//             <img
//               className="icon"
//               src="/assets/icons/preparationTime-icon.svg"
//               alt=""
//             />
//             <span>{prepTime}</span>
//           </div>
//           <div class="col-6 col-xl-3 ps-3">
//             <img
//               className="icon"
//               src="/assets/icons/cookingTime-icon.svg"
//               alt=""
//             />
//             <span>{cookingTime}</span>
//           </div>
//           <div class="col-6 col-xl-3">
//             <img
//               className="icon"
//               src="/assets/icons/servings-icon.svg"
//               alt=""
//             />
//             <span>{serving}</span>
//           </div>
//           <div class="col-6 col-xl-3 pe-5">
//             {veg ? (
//               <img className="icon" src="/assets/icons/veg-icon.svg" alt="" />
//             ) : (
//               <img
//                 className="icon"
//                 src="/assets/icons/nonveg-icon.svg"
//                 alt=""
//               />
//             )}
//           </div>
//         </div>
//         <div className="text-start p-3">
//           <h1>Nutrition Facts</h1>
//           <table class="table table-dark table-striped">
//             <tbody>
//               <tr>
//                 <th scope="row">Fat</th>
//                 <td>{nutrientFacts["fat"]}</td>
//               </tr>
//               <tr>
//                 <th scope="row">Protein</th>
//                 <td>{nutrientFacts["protein"]}</td>
//               </tr>
//               <tr>
//                 <th scope="row">Sugar</th>
//                 <td colSpan="2">{nutrientFacts["sugar"]}</td>
//               </tr>
//               <tr>
//                 <th scope="row">Carbs</th>
//                 <td colSpan="2">{nutrientFacts["carbo"]}</td>
//               </tr>
//             </tbody>
//           </table>
//         </div>
//       </div>
//     </>
//   );
// }

// export default FoodItem;

import React from "react";
import "../App.css";

function FoodItem({ name, description, nutrientFacts, veg, prepTime, cookingTime, serving }) {
  const pngFoods = ["Kulfi", "Samosa"];
  const ext = pngFoods.includes(name) ? "png" : "jpg";
  const imgPath = `/assets/foodImages/${name}.${ext}`;

  return (
    <>
      <div className="col-12 col-md-6 food-image-wrap">
        <img src={imgPath} className="food-pic" alt={name} />
      </div>
      <div className="col-12 col-md-6 food-info">
        <h1 className="food-name">{name !== "Default" ? name : "Your Next Meal"}</h1>
        <p className="food-description">{description}</p>

        <div className="food-meta">
          <div className="meta-item">
            <img src="/assets/icons/preparationTime-icon.svg" alt="prep" />
            <span>{prepTime}</span>
          </div>
          <div className="meta-item">
            <img src="/assets/icons/cookingTime-icon.svg" alt="cook" />
            <span>{cookingTime}</span>
          </div>
          <div className="meta-item">
            <img src="/assets/icons/servings-icon.svg" alt="serves" />
            <span>{serving}</span>
          </div>
          <div className="meta-item">
            {veg ? (
              <img className="icon" src="/assets/icons/veg-icon.svg" alt="veg" />
            ) : (
              <img className="icon" src="/assets/icons/nonveg-icon.svg" alt="non-veg" />
            )}
          </div>
        </div>

        <h2 className="nutrition-title">Nutrition Facts</h2>
        <table className="table table-dark table-striped rounded overflow-hidden">
          <tbody>
            <tr><th scope="row">Fat</th><td>{nutrientFacts["fat"]}</td></tr>
            <tr><th scope="row">Protein</th><td>{nutrientFacts["protein"]}</td></tr>
            <tr><th scope="row">Sugar</th><td>{nutrientFacts["sugar"]}</td></tr>
            <tr><th scope="row">Carbs</th><td>{nutrientFacts["carbo"]}</td></tr>
          </tbody>
        </table>
      </div>
    </>
  );
}

export default FoodItem;

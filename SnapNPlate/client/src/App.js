// import React, { useEffect, useState } from "react";
// import "./App.css";
// import foodData from "./data/Fooddata.json";
// import FoodItem from "./components/FoodItem";
// import Instructions from "./components/Instructions";
// import Ingredients from "./components/Ingredients";
// import Footer from "./components/Footer";
// import ImageUpload from "./components/ImageUpload";

// function App() {
//   const [data, setData] = useState({ class: "Default", confidence: 100 });
//   const [food, setFood] = useState(foodData["Default"]);
//   const [err, setErr] = useState(false);

//   useEffect(() => {
//     setFood(foodData[data.class]);
//   }, [data]);

//   return (
//     <div className="App">
//       <nav
//         class="navbar bg-dark border-bottom border-body"
//         data-bs-theme="dark"
//       >
//         <div class="container-fluid">
//           <a class="navbar-brand" href="#">
//             <img src="/assets/favicon.ico" className="pe-3" />
//             SnapNPlate
//           </a>
//         </div>
//       </nav>
//       {err && (
//         <div class="alert alert-secondary" role="alert">
//           We couldn't confidently classify the provided image based on our
//           current dataset. Please ensure the photo is clear and well-lit, or try
//           another angle for a more accurate classification. If the issue
//           persists, it may be a unique or uncommon food item not currently in
//           our database. Thank you for your understanding.
//         </div>
//       )}
//       <div className="row">
//         <FoodItem
//           name={data.class}
//           description={food["description"]}
//           nutrientFacts={food["nutrientfact"]}
//           veg={food["veg"]}
//           prepTime={food["preptime"]}
//           cookingTime={food["cookingtime"]}
//           serving={food["serving"]}
//         />
//       </div>
//       <div className="row">
//         <ImageUpload setData={setData} setErr={setErr} />
//       </div>
//       <div className="row">
//         <div className="col-12 col-xl-6">
//           <Instructions instructions={food["instruction"]} />
//         </div>
//         <div className="col-12 col-xl-6">
//           <Ingredients ingredients={food["ingredients"]} />
//         </div>
//       </div>
//       <Footer />
//     </div>
//   );
// }

// export default App;
import React, { useEffect, useState } from "react";
import "./App.css";
import foodData from "./data/Fooddata.json";
import FoodItem from "./components/FoodItem";
import Instructions from "./components/Instructions";
import Ingredients from "./components/Ingredients";
import Footer from "./components/Footer";
import ImageUpload from "./components/ImageUpload";

function App() {
  const [data, setData] = useState({ class: "Default", confidence: 100 });
  const [food, setFood] = useState(foodData["Default"]);
  const [err, setErr] = useState(false);

  useEffect(() => {
    setFood(foodData[data.class]);
  }, [data]);

  return (
    <div className="App">
      <nav
        class="navbar bg-dark border-bottom border-body"
        data-bs-theme="dark"
      >
        <div class="container-fluid">
          <a class="navbar-brand" href="/">
            <img src="/assets/favicon.ico" className="pe-3" alt="SnapNPlate logo" />
            SnapNPlate
          </a>
        </div>
      </nav>
      {err && (
        <div class="alert alert-secondary" role="alert">
          We couldn't confidently classify the provided image based on our
          current dataset. Please ensure the photo is clear and well-lit, or try
          another angle for a more accurate classification. If the issue
          persists, it may be a unique or uncommon food item not currently in
          our database. Thank you for your understanding.
        </div>
      )}
      <div className="row">
        <FoodItem
          name={data.class}
          description={food["description"]}
          nutrientFacts={food["nutrientfact"]}
          veg={food["veg"]}
          prepTime={food["preptime"]}
          cookingTime={food["cookingtime"]}
          serving={food["serving"]}
        />
      </div>
      <div className="row">
        <ImageUpload setData={setData} setErr={setErr} />
      </div>
      <div className="row">
        <div className="col-12 col-xl-6">
          <Instructions instructions={food["instruction"]} />
        </div>
        <div className="col-12 col-xl-6">
          <Ingredients ingredients={food["ingredients"]} />
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default App;

// import React, { useEffect, useState } from "react";
// import "./App.css";
// import foodData from "./data/Fooddata.json";
// import FoodItem from "./components/FoodItem";
// import Instructions from "./components/Instructions";
// import Ingredients from "./components/Ingredients";
// import Footer from "./components/Footer";
// import ImageUpload from "./components/ImageUpload";

// function App() {
//   const [data, setData] = useState({ class: "Default", confidence: 100 });
//   const [food, setFood] = useState(foodData["Default"]);
//   const [err, setErr] = useState(false);

//   useEffect(() => {
//     setFood(foodData[data.class]);
//   }, [data]);

//   return (
//     <div className="App">
//       <nav className="snap-navbar">
//         <a className="snap-brand" href="/">
//           <img src="/assets/favicon.ico" alt="SnapNPlate logo" />
//           SnapNPlate
//         </a>
//       </nav>

//       {err && (
//         <div className="snap-alert" role="alert">
//           We couldn't confidently identify this food. Please try a clearer, well-lit photo of one of our supported dishes.
//         </div>
//       )}

//       <div className="row g-0 food-card">
//         <FoodItem
//           name={data.class}
//           description={food["description"]}
//           nutrientFacts={food["nutrientfact"]}
//           veg={food["veg"]}
//           prepTime={food["preptime"]}
//           cookingTime={food["cookingtime"]}
//           serving={food["serving"]}
//         />
//       </div>

//       <div className="upload-section">
//         <ImageUpload setData={setData} setErr={setErr} />
//       </div>

//       <div className="row g-0">
//         <div className="col-12 col-xl-6">
//           <Instructions instructions={food["instruction"]} />
//         </div>
//         <div className="col-12 col-xl-6" style={{borderLeft: "1px solid #e8e0d5"}}>
//           <Ingredients ingredients={food["ingredients"]} />
//         </div>
//       </div>

//       <Footer />
//     </div>
//   );
// }

// export default App;

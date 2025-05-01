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
          <a class="navbar-brand" href="#">
            <img src="/assets/favicon.ico" className="pe-3" />
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

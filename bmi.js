function calculateBMI() {

    let weight = parseFloat(document.getElementById("weight").value);
    let height = parseFloat(document.getElementById("height").value) / 100;

    let result = document.getElementById("result");

    // Validation
    if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {
        result.style.color = "red";
        result.innerHTML = "Please enter valid height and weight.";
        return;
    }

    let bmi = weight / (height * height);
    bmi = bmi.toFixed(2);

    result.style.color = "#00ff99";

    if (bmi < 18.5) {
        result.innerHTML = "Underweight <br>BMI: " + bmi;
    }
    else if (bmi >= 18.5 && bmi <= 24.9) {
        result.innerHTML = "Normal Weight <br>BMI: " + bmi;
    }
    else if (bmi >= 25 && bmi <= 29.9) {
        result.innerHTML = "Overweight <br>BMI: " + bmi;
    }
    else {
        result.innerHTML = "Obese <br>BMI: " + bmi;
    }

}
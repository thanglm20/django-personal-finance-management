
const passwordField = document.querySelector("#passwordField");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const cofirmPasswordField = document.querySelector("#CofirmPasswordField");
const correctPassword = document.querySelector(".CorrectPassword");
const correctPasswordConfirm = document.querySelector(".CorrectPasswordConfirm");

const submitBtn = document.querySelector(".submit-btn");


const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === "SHOW") {
    showPasswordToggle.textContent = "HIDE";
    passwordField.setAttribute("type", "text");
  } else {
    showPasswordToggle.textContent = "SHOW";
    passwordField.setAttribute("type", "password");
  }
};
cofirmPasswordField.setAttribute("type", "password");

showPasswordToggle.addEventListener("click", handleToggleInput);

passwordField.addEventListener("keyup", (e) => {
  const pwd = passwordField.value;
  if(pwd == ""){
    correctPassword.style.display = "block";
    correctPassword.style.color = "red";
    correctPassword.innerHTML = `<p>Password is not empty</p>`;
    document.getElementById('set_password').disabled = true;
  }
  else{
    correctPassword.style.color = "green";
    correctPassword.innerHTML = `<p>Password is valid</p>`;
  }
 
});



cofirmPasswordField.addEventListener("keyup", (e) => {
  const pwd = passwordField.value;
  const confirm_password = e.target.value;
  if(pwd != confirm_password){
    correctPasswordConfirm.style.display = "block";
    correctPasswordConfirm.style.color = "red";
    correctPasswordConfirm.innerHTML = `<p>Password is not matched</p>`;
    document.getElementById('set_password').disabled = true;
  }
  else{
    correctPasswordConfirm.style.color = "green";
    correctPasswordConfirm.innerHTML = `<p>Password is matched</p>`;
    document.getElementById('set_password').disabled = false;
  }
});



function onBtnResetClicked(){

  const pwd = passwordField.value;
  const confirm_password = cofirmPasswordField.value;
  if(pwd == ""){
    correctPassword.style.display = "block";
    correctPassword.style.color = "red";
    correctPassword.innerHTML = `<p>Password is not empty</p>`;
    document.getElementById('set_password').disabled = true;

    return false;
  }
  else if(confirm_password==""){
    correctPasswordConfirm.style.display = "block";
    correctPasswordConfirm.style.color = "red";
    correctPasswordConfirm.innerHTML = `<p>Password is not match</p>`;
    document.getElementById('set_password').disabled = true;
    return false;
  }
  else if(pwd != confirm_password){
    alert("Password is not matched");
    document.getElementById('set_password').disabled = true;
    return false;
  }
  return true
}
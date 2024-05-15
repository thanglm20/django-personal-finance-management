const emailField = document.querySelector("#emailField");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const submitBtn = document.querySelector(".submit-btn");

emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;

  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/authen/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if(data.email_used){
          emailField.classList.add("is-valid");
          emailFeedBackArea.style.display = "block";
          emailFeedBackArea.style.color = "green";
          emailFeedBackArea.innerHTML = `<p>This email is correct, please click "Reset password" and check your email!!!</p>`;
        }
        if (data.email_invalid || data.email_valid) {
          submitBtn.disabled = true;
          emailField.classList.add("is-invalid");
          emailFeedBackArea.style.display = "block";
          emailFeedBackArea.style.color = "red";
          emailFeedBackArea.innerHTML = `<p>This email is invalid or unregistered</p>`;
        
        }
        else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});
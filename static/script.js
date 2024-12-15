document.addEventListener("DOMContentLoaded", () => {
  const smsInput = document.getElementById("smsInput");
  const submitButton = document.getElementById("submitButton");
  const loadingMessage = document.getElementById("loadingMessage");
  const resultDiv = document.getElementById("result");

  submitButton.addEventListener("click", () => {
    const smsText = smsInput.value.trim();
    // Clear previous results
    resultDiv.style.display = "none";
    resultDiv.className = "";
    resultDiv.textContent = "";

    // Check if input is empty
    //if (!smsText) {
     // alert("Please type an SMS message before submitting.");
     // return;
    //}

    // Show loading message
    loadingMessage.style.display = "block";

    // Send SMS text to Flask backend
    fetch("http://127.0.0.1:5000/classify", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ sms: smsText }),
    })
      .then((response) => response.json())
      .then((data) => {
        loadingMessage.style.display = "none";

        if (data.error) {
          alert(data.error);
          return;
        }

        const isSpam = data.is_spam;
        resultDiv.style.display = "block";
        if (isSpam) {
          resultDiv.textContent = "This SMS is classified as SPAM.";
          resultDiv.classList.add("spam");
        } else {
          resultDiv.textContent = "This SMS is NOT SPAM.";
          resultDiv.classList.add("not-spam");
        }
      })
      .catch((error) => {
        loadingMessage.style.display = "none";
        alert("An error occurred while processing the SMS.");
        console.error(error);
      });
  });
});

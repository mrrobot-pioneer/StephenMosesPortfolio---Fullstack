/*=========== submit contact form via js ============*/

const contactBtn = document.getElementById("contact-form");

contactBtn.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the default form submission

  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const userName = document.querySelector('input[name="user_name"]').value;
  const userEmail = document.querySelector('input[name="user_email"]').value;
  const userMessage = document.querySelector(
    'textarea[name="user_message"]'
  ).value;

  const contactMessageElement = document.getElementById("contact-message");

  // Show a "sending..." message
  contactMessageElement.textContent = "Sending message...";

  fetch("https://stephenmoses.primeelements.pro/contact/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      name: userName,
      email: userEmail,
      message: userMessage,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      contactMessageElement.textContent =
        "Your message has been sent successfully! I will get back to you soonest.";

      // Clear form fields
      document.querySelector('input[name="user_name"]').value = "";
      document.querySelector('input[name="user_email"]').value = "";
      document.querySelector('textarea[name="user_message"]').value = "";
    })
    .catch((error) => {
      contactMessageElement.textContent =
        "Error sending message. Please try again later.";
    });
});

/*=============== SHOW SCROLL UP ===============*/
const scrollup = () => {
  const scrollup = document.getElementById("scroll-up");
  this.scrollY >= 250
    ? scrollup.classList.add("show-scroll")
    : scrollup.classList.remove("show-scroll");
};

window.addEventListener("scroll", scrollup);

/*=========== Dark/Light mode toggler */
const toggler = document.querySelector(".toggler");
toggler.addEventListener("click", toggleTheme);

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute("data-theme");
  if (currentTheme === "dark") {
    document.documentElement.setAttribute("data-theme", "light");
  } else {
    document.documentElement.setAttribute("data-theme", "dark");
  }
}

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll("section[id]");

const scrollActive = () => {
  const scrollDown = window.scrollY;

  sections.forEach((current) => {
    const sectionHeight = current.offsetHeight,
      sectionTop = current.offsetTop - 58,
      sectionId = current.getAttribute("id"),
      sectionClass = document.querySelector(
        ".nav__list a[href*=" + sectionId + "]"
      );

    if (scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight) {
      sectionClass.classList.add("active-link");
    } else {
      sectionClass.classList.remove("active-link");
    }
  });
};

window.addEventListener("scroll", scrollActive);

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
  origin: "top",
  distance: "60px",
  duration: 2500,
  delay: 200,
  // reset: true, //make the animations repeat everytime they enter the view port
});

sr.reveal(".perfil,.contact__form");
sr.reveal(".info", { origin: "left", delay: 600 });
sr.reveal(".skills", { origin: "left", delay: 900 });
sr.reveal(".about", { origin: "right", delay: 1000 });
sr.reveal(".projects__card, .services__card,.experience__card", {
  interval: 100,
});

/*=============== EMAIL JS ===============*/
const contactForm = document.getElementById("contact-form");
const contactMessage = document.getElementById("contact-message");

const sendEmail = (e) => {
  e.preventDefault();

  //   serviceId,templateId, formId, publicKey

  emailjs
    .sendForm(
      "service_a4rru6e",
      "template_elhed8g",
      "#contact-form",
      "DIMyqkkw8WKqNPCYX"
    )

    .then(
      () => {
        // show send message
        contactMessage.textContent = "Message sent successfully ✅";

        // remove message after five seconds
        setTimeout(() => {
          contactMessage.textContent = "";
        }, 5000);

        //   clear input fields
        contactForm.reset();
      },
      () => {
        // show error message
        contactMessage.textContent =
          "An error occurred while sending this message ❌";
      }
    );
};

contactForm.addEventListener("submit", sendEmail);

/*=============== SHOW SCROLL UP ===============*/
const scrollup = () => {
  const scrollup = document.getElementById("scroll-up");
  this.scrollY >= 250
    ? scrollup.classList.add("show-scroll")
    : scrollup.classList.remove("show-scroll");
};

window.addEventListener("scroll", scrollup);

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
sr.reveal(".skills", { origin: "left", delay: 8000 });
sr.reveal(".about", { origin: "right", delay: 1000 });
sr.reveal(".projects__card, .services__card,.experience__card", {
  interval: 100,
});

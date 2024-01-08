const githubherf = document.querySelector(".githubherf");
const githubButton = document.querySelector(".githubButton");

githubButton.addEventListener("click", () => {
    githubherf.click();
});

const line1 = document.querySelector(".line1");
const line2 = document.querySelector(".line2");
const line3 = document.querySelector(".line3");
const nav_menu = document.querySelector(".nav_menu");
const nav__list = document.querySelector(".nav__list");
const nav__buttons = document.querySelector(".nav__buttons");

nav_menu.addEventListener("click", () => {
    nav__buttons.classList.toggle("active");
    nav__list.classList.toggle("active");
    line1.classList.toggle("active");
    line2.classList.toggle("active");
    line3.classList.toggle("active");
});

const projectsButton = document.querySelector(".ProjectButton");

projectsButton.addEventListener("click", (event) => {
    event.preventDefault(); 

    const projectsSection = document.querySelector("#Project");

    if (projectsSection) {
        projectsSection.scrollIntoView({
            behavior: "smooth"
        });
    }
});

window.addEventListener("load", () => {
    document.querySelector("main").style.display = "block";
    document.querySelector(".load").style.display = "none";
});

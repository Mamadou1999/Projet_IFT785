/* main.js - Script principal pour Adopte un Dev */

document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript chargé avec succès !");
  
    // Gestion du menu mobile
    const menuToggle = document.getElementById("menu-toggle");
    const navbarMenu = document.getElementById("navbar-menu");
  
    if (menuToggle && navbarMenu) {
      menuToggle.addEventListener("click", function () {
        navbarMenu.classList.toggle("show");
      });
    }
  
    // Confirmation avant suppression d'un élément
    document.querySelectorAll(".delete-btn").forEach(button => {
      button.addEventListener("click", function (event) {
        if (!confirm("Êtes-vous sûr de vouloir supprimer cet élément ?")) {
          event.preventDefault();
        }
      });
    });
  });
  
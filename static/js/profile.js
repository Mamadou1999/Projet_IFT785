/* profile.js - Gestion des interactions sur la page de profil */

document.addEventListener("DOMContentLoaded", function () {
    console.log("Script profile.js chargé avec succès !");
  
    // Gestion de l'édition du profil
    const editButton = document.getElementById("edit-profile-btn");
    const saveButton = document.getElementById("save-profile-btn");
    const profileFields = document.querySelectorAll(".profile-field");
  
    if (editButton && saveButton) {
      editButton.addEventListener("click", function () {
        profileFields.forEach(field => field.removeAttribute("disabled"));
        saveButton.classList.remove("d-none");
        editButton.classList.add("d-none");
      });
  
      saveButton.addEventListener("click", function () {
        profileFields.forEach(field => field.setAttribute("disabled", "true"));
        saveButton.classList.add("d-none");
        editButton.classList.remove("d-none");
        alert("Modifications enregistrées avec succès !");
      });
    }
  });
  
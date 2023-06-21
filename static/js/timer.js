document.addEventListener("DOMContentLoaded", function() {
    function changeContainerColor() {
      var select = document.getElementById("corParada");
      var maquinaContainer = document.getElementById("conteudoMaquina");

      var selectedColor = select.value;

      var selectedText = select.options[select.selectedIndex].getAttribute("data-text");

      maquinaContainer.style.backgroundColor = selectedColor;

      maquinaContainer.textContent = selectedText;
    }

    document.getElementById("corParada").addEventListener("change", changeContainerColor);


    document.getElementById("save").addEventListener("click", changeContainerColor);
  });

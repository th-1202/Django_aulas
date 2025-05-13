// Função que pergunta o usúario se ele quer mesmo excluir a Tarefa//


document.querySelectorAll(".delete-btn").forEach(
    btn => {
        btn.addEventListener("click", function(e) {
            e.preventDefault();

            const delLink = this.getAttribute("href");

            if(delLink && confirm("quer deletar esta tarefa ?")){
                window.location.href = delLink
            }


            
        });
    }
);
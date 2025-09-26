const lis = document.querySelector("#listinha");

fetch('http://localhost:8000/listarfilmes').then((res)=>{
    return res.json();
}).then((filmes)=>{
    filmes.map((lista)=>{
        console.log(lista)
        lis.innerHTML += `
        <li>
            <img src= "${lista.capa}"/> <br>
            <strong>Nome do Filme: </strong> ${lista.nome} </br>
            <strong>Atores: </strong> ${lista.atores} </br>
            <strong>Diretor: </strong> ${lista.diretor} </br>
            <strong>Ano: </strong> ${lista.ano} </br>
            <strong>Genero: </strong> ${lista.genero} </br>
            <strong>Produtora: </strong> ${lista.produtora} </br>
            <strong>Sinopse: </strong> ${lista.sinopse} </br>
        </li>
        `
    })
})
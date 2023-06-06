const searchWrapper = document.querySelector('.search');
const inputBox = searchWrapper.querySelector('input');
const icon = searchWrapper.querySelector('.icon');
let linkTag = searchWrapper.querySelector('a');
let webLink;

// criando um evento 
inputBox.onkeyup = (e) => {
    let userData = e.target.value;

    // Se a tecla enter for pessionada 
    if (e.key == 'Enter') {
        if (userData) {
            window.open(`https://www.google.com/search?q=${userData}`, '_blanck');
        }
    }

    // Se a lupa for clicada if(userData) { 
    icon.onclick = () => {
        webLink = `https://www.google.com/search?q=${userData}`;
        linkTag.setAttribute('href', webLink);
        linkTag.click();
    }
} 
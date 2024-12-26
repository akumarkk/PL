let board = document.querySelector('.board');
let start = false;
let end = false;
let path = new Map();

board.addEventListener('click', (e) => {
    console.log(`${start} ${end}`);
    if (!start) {

        path.set(e.target, e.target.style.backgroundColor);
        start = e.target;
        e.target.style.backgroundColor = 'red';
        
    } else if (start) {
        // Additionally as a bonus, you can also try to refresh the board if the user clicks on some other checkbox, and then trace the path from the new checkbox. (Code for this is provided in the solution)

        path.forEach((color, element) => {
            element.style.backgroundColor = color;
            path.delete(element);
        });
        
        start = e.target;
        path.set(e.target, e.target.style.backgroundColor);
        e.target.style.backgroundColor = 'red';
        console.log("end clicked");
        // end.style.backgroundColor = 'yellow';
    }
    
    else if (!end) {
        if(!path.has(e.target)) {
            path.set(e.target, e.target.style.backgroundColor);
        }
        
        end = true;
        e.target.style.backgroundColor = 'red';
        console.log("end clicked");
        // end.style.backgroundColor = 'yellow';
    } else {
        path.forEach((color, element) => {
            element.style.backgroundColor = color;
        });
        start = null;
        end = false;
    }

});

board.addEventListener('mouseover', (e) => {


    if (!start) {
        return;

    }

    if(path.has(e.target)) {
        return;
    }

    let x = parseInt(e.target.parentElement.id) - parseInt(start.parentElement.id);
    let y = (parseInt(e.target.id) % 8 == 0 ? 8 : parseInt(e.target.id) % 8)
        - (parseInt(start.id) % 8 == 0 ? 8 : parseInt(start.id) % 8);

    if (Math.abs(x) == Math.abs(y)) {
        path.set(e.target, e.target.style.backgroundColor);
        e.target.style.backgroundColor = 'red';
        start = e.target;
    }
});
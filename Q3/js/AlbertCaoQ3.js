ratingWidget();

// Big ol' function for the Rating Widget.
async function ratingWidget() {
    // Grab product ID.
    const widgetId = document.currentScript.id;
    const widgetClass = "." + widgetId;

    defer();
    
    function defer(method) {
        if (window.jQuery) {
            init($);
            return;
        }
        else {
            var script = document.createElement("script");
            script.type = "text/javascript";
            script.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js";
            document.getElementsByTagName("head")[0].appendChild(script);
            
            setTimeout(function() {defer(method); }, 50);
        }
    }
    
    function init($) {
        // The HTML for the rating widget.
        let starHtml = 
            `<ul class="list-inline rating-list">
            <li id="5-stars" class="star" onmouseover="mouseOver(this)" onmouseout="mouseOut(this)" onclick="mouseClick(this)">☆</li>
            <li id="4-stars" class="star" onmouseover="mouseOver(this)" onmouseout="mouseOut(this)" onclick="mouseClick(this)">☆</li>
            <li id="3-stars" class="star" onmouseover="mouseOver(this)" onmouseout="mouseOut(this)" onclick="mouseClick(this)">☆</li>
            <li id="2-stars" class="star" onmouseover="mouseOver(this)" onmouseout="mouseOut(this)" onclick="mouseClick(this)">☆</li>
            <li id="1-star" class="star" onmouseover="mouseOver(this)" onmouseout="mouseOut(this)" onclick="mouseClick(this)">☆</li>
            </ul>`;
            
        $(widgetClass).append(starHtml);
    }
}

// On mouse over...
function mouseOver(e) {    
    $(e).text("★");
    $(e).nextAll().text("★");
}

// On mouse out...
function mouseOut(e) {
    $(e).text("☆");
    $(e).nextAll().text("☆");
}
  
// On mouse click...
function mouseClick(e) {
// Setting star colors to black to indicate final rating.
    $(e).css("color", "black");
    $(e).nextAll().css("color", "black");

    // Grabbing details on the rating and product.
    var thisId = $(e).attr('id');
    var thisList = $(e).parent().children();
    var productId = $(e).parent().parent().siblings().prev(".productId").attr("id");

    // Debugging.
    console.log(thisId);
    console.log(productId);

    // Removing mouseover/out/click event listeners from each star to prevent further rating.
    for (let i = 0; i < thisList.length; i++) {
        thisList[i].removeAttribute("onmouseover");
        thisList[i].removeAttribute("onmouseout");
        thisList[i].removeAttribute("onclick");
    }

    // The HTML for the feedback text.
    let thankHtml = 
    `<div class="alert alert-success" role="alert">
        Thanks for rating!
    </div>`;

    $(e).parent().parent().append(thankHtml);

    // Compiling data into the correct format.
    var results = {
        "rating": thisId, // Placeholder for rating
        "product": productId // Placeholder for productId
    };

    // POSTing rating to the server.
    $.ajax({
        url: "https://reqres.in/api/users",
        type: "POST",
        data: results,
        success: function(e) {
            alert("Rating recorded!")
            console.log("Success!");
            console.log(e);
        },
        error: function(e) {
            console.error("Error!");
        }
    });
} 

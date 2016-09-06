chrome.extension.sendMessage({}, function(response) {

	stopWords = {'commenting':1,
				'great':5}

	function huntTrolls(){
		var comments = $('.comment-renderer-text-content');
      	comments.each(function() {
      		commentScore = rateComment($(this).text().toLowerCase());
      		if (commentScore > 0){
      			actionOnTrollComment(this,commentScore);
				}
		});     
	}

	function actionOnTrollComment(trollComment,score){

		console.log($( trollComment ).text()  +' score: '+ score);
  		$(trollComment)
	  		.closest(".comment-renderer")
	  		.parent()
	  		.css("background-color", "yellow");
  		// $(".comment-renderer").hide();
	}

	function rateComment(comment){
		var score = 0;
		for (var word in stopWords) {
		    if (stopWords.hasOwnProperty(word)) {
		        if (comment.indexOf(word) !== -1)
		        	score += stopWords[word]
		    }
		}
		return score
	}

	  function pollVisibility() {
      if (!$(".action-panel-loading").is(":visible")) {
          // call a function here, or do whatever now that the div is not visible
		  huntTrolls();
      } else {
          setTimeout(pollVisibility, 500);
      }
  	}

	var readyStateCheckInterval = setInterval(function() {
	if (document.readyState === "complete") {
		clearInterval(readyStateCheckInterval);

		// ----------------------------------------------------------
		// This part of the script triggers when page is done loading
		console.log("Hello. This message was sent from scripts/inject.js");
		// ----------------------------------------------------------

		pollVisibility();
	}
	}, 10);
});

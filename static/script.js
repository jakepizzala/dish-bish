function getRank(user_id) {

}

function getRandomPun(rank) {
    if (rank === "False") {
        return;
    }
	var puns = [
		"Seems like we got a new Clean Queen!",
		"You're a real Rinse Prince over there!",
		"WATCH OUT! There's a Sponge Samari on the loose!",
		"You trying to be some kind of SOAPer bowl champ over there or something?",
		"All that hard trabajo has made you a proper Chore Señor!",
		"Knife going over there!",
		"May the fork be with you.",
		"NICE! Your enthusiasm has proven you're not just some casual glass kisser.",
		"You really CUP to the chase with that one.",
		"You make me feel so clean.",
		"You can really DISH it as well as you can take it, can't you?",
		"Woohoo! Aren't you just loads of fun.",
		"Soaper job, you Sudspert!",
		"A regular Kitchen's Pet over there. I approve.",
		"That was a regular Soapy's Choice situation, but you made the right call.",
		"Way to wipe up that ugly mug!",
		"WHAT THE FORK! Oh, just you again. Don't sneak up on me like that.",
		"I had a SINKing feeling you'd never get here, but I'm glad you did!",
		"You're still a lazy forker, but there's still hope for you."
	];
	if (rank == 1) {
		return "You da Top Dish Bish, that's what you is! Make a wish!";
	} else if (rank == 2) {
		return "CLEANOPATRA! You will not be triumphed over!";
	} else if (rank == 3) {
		return "You're the greatest, Chorelie Brown!";
	} else {
		var index = Math.floor(Math.random() * puns.length);
		return puns[index];
	}
}


$(document).ready(function(){
    var rank = $(".rank").html();
    var pun = getRandomPun(rank);
    $('.message-text').html(pun);
    $('#name').change(function() {
        $('.task-button').removeAttr('disabled');
    })

    $('.task-button').click(function(e) {
        e.preventDefault();
        var task = e.target.value;
        $('#task').val(task);
        $("#task-form").submit();
    })
});

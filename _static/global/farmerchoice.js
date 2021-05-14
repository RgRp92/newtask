// Making a top level namespace for beliefs
let beliefs_ns = new function() {

let non_assegnati = 0;

// Helper functions
// Quadratic Scoring Rule
let qsr = function(bin) {
	let a = 12.5;
	let b = 12.5;
	let num_bins = 10;
	let tokens = 100;
	let outcome = 0;
	for (let i = 1; i <= num_bins ; i++) {
		let report = Number($("#bin" + i).val()) / tokens;
		outcome -= (report * report);
		if (i == bin) {
			outcome += (2 * report);
		}
	}
	outcome = a + b * outcome;
	outcome *= 100;
	outcome = Math.round(outcome) / 100;
	return outcome;
}

// Calculate how many tokens are allocated outside of a bin
let other_bin_tokens = function(bin) {
	let count = 0;
	for (i = 1; i <= beliefs_ns.beldat["num_bins"] ; i++) {
		if (i == bin) continue
		count += Number($("#bin" + i).val());
	}
	return(count)
}

// Add an s if 1
let pluralizer = function(x) {
	return (x == 1 ? "" : "s")
}


// Fit the slider underneath the bars
let fix_slider_position = function() {
	let cw = $(".cell_val").width();
	let ch = $(".cell_val").height();
	let sh = $(".slider").height();
	let num_bins = beliefs_ns.beldat["num_bins"];
	console.log(num_bins);

	let sw = .9 * ch;
	$(".slider").css("width", sw + "px");

	// Need to accommodate the bottom offset
	sh = parseFloat(sh)
	sw = parseFloat(sw)

	// Where to place the sliders
	let sb = sw / 2;
	sb -= 0.1 * sb
	let ml = -sb - (sh / sw) + cw / 2 - sh/2;

	// Set the bottom based on the width
	$(".slider").css("bottom", sb + "px")
	for (let i = 1 ; i <= num_bins; i++ ) {
		$("#bin" + i).css("left", ml + "px");
	}
}

// Submit the form or give message
let submit_click = function() {
	if (non_assegnati == 0) {
		$("#submit_button").prop("type", "");
	}
}


this.submit_click = function () {
	log_event('submit');
}

// The reaction function for when a slider is moved
let set_token_allocations = function(bin, beldat) {
	let this_bin  = Number($("#bin" + bin).val());
	let other_bin = Number(other_bin_tokens(bin));
	let amt = [];
	let max_earnings = beldat["alpha"] + beldat["delta"];
	let tokens = beldat["tokens"]
	let currency = beldat["currency"]


	if ((this_bin + other_bin) > tokens) {
		this_bin = tokens - other_bin;
		$("#bin" + bin).val(this_bin);
	}

	// bar_amt height needs to be in percentage
	let bar_amt_h = parseFloat($(".bar_amt").css("height"))
	let bar_div_h = parseFloat($("#bar_div").css("height"))
	let ratio = bar_amt_h / bar_div_h

	for (i = 1; i <= beldat["num_bins"] ; i++) {
		amt[i] = qsr(i);

		let bval = (100 * amt[i] / max_earnings) * (1 - ratio)
		let aval = currency + amt[i]

		$("#amt" + i).html(aval);
		$("#bar" + i).css("height", bval + "%");
		$("#bar_amt" + i).css("bottom", bval + "%");
		$("#bar_amt" + i).html(aval);
	}
	// The number of tokens allocated to this bin
	$("#prob" + bin).html(this_bin + " gettoni");
	// The number of non_assegnati tokens
	non_assegnati = tokens - this_bin - other_bin;
	if (non_assegnati == 0) {
		$("#submit_button").prop('disabled', false);
		$("#submit_message").html("&nbsp;");
	} else {
		$("#submit_button").prop('disabled', true);
		$("#submit_message").html("Tutti i gettoni devono essere assegnati.");
	}
	$("#non_assegnati").html(non_assegnati);
}

// Function to set axis ticks
let axis_stuff = function(beldat) {
	$("#axis_div").css("height", "100%");


	// bar height is adjusted based to deal with the text vals
	let bar_amt_h = parseFloat($(".bar_amt").css("height"));
	let bar_div_h = parseFloat($("#bar_div").css("height"));

	// The % of space that is taken up by the amounts over the bars
	let amt_text_vspace = bar_amt_h / (bar_div_h);

	// The axis will start at alpha minus delta
	let minval = beldat["alpha"] - beldat["delta"];
	let maxval = beldat["alpha"] + beldat["delta"];

	// Fill the html
	let inhtml = "<div class='axis_tick' style='";
	let this_html = "";

	// The number of ticks MINUS ONE. The ticks above the minimum
	let num_ticks = 4;

	for (let i = 0; i < num_ticks + 1 ; i++) {
		let real_percent = (i * 100 / num_ticks);
		let bottom = (real_percent - 5) * (1 - amt_text_vspace);
		// Add 2 percent for the border of the big div and the white border on
		// the bars
		bottom += 2;

		// The actual amount on the axis
		let displayed = minval +  i * (maxval - minval) / num_ticks;
		displayed = beldat["currency"] + displayed + "";
		this_html += "<div class='axis_tick' style='";
		this_html += "bottom:" + bottom + "%;'>";
		this_html += displayed + "</div>\n";
	}
	// Set the ticks
	$("#axis_div").html(this_html);
}

let beliefs_add_content = function(num_bins, tokens, divid, results = 0, show_submit = 1) {
	let inhtml = ""
	if (results == 1) {
		inhtml += "<div id=\"results_text\">\n";
		if (show_submit == 1) {
			inhtml += "<br>\n";
		}
		inhtml += "<br>\n";
		inhtml += "</div>\n";
	}
	inhtml += "<div id=\"top_div\">\n";
	inhtml += "<div id=\"question_div\"></div>\n";
	inhtml += "<div id=\"chart_wapper\">\n";
	inhtml += "<div id=\"bar_div\">\n";
	inhtml += "<div id=\"axis_div\"></div>\n";

	for (let i = 1 ; i <= num_bins ; i++) {
		inhtml += "<div class=\"bar_amt\" id=\"bar_amt" + i + "\">0</div>\n";
		inhtml += "<div class=\"div_bar\" id=\"bar" + i + "\"> </div>\n";
	}
	inhtml += "</div>\n";
	inhtml += "</div>\n";
	inhtml += "<div id=\"label_div\">\n";
	for (let i = 1 ; i <= num_bins ; i++) {
		inhtml += "<div class=\"label_val\" id=\"label" + i + "\" ></div>\n";
	}
	inhtml += "</div>\n";
	inhtml += "<div id=\"non_assegnati\">" + tokens + "</div>\n";
	inhtml += "<div id=\"prob_div\">\n";
	for (let i = 1 ; i <= num_bins ; i++) {
		inhtml += "<div class=\"prob_val\" id=\"prob" + i + "\" ></div>\n";
	}
	inhtml += "</div>\n";
	inhtml += "<div id=\"amount_div\">\n";
	for (let i = 1 ; i <= num_bins ; i++) {
		inhtml += "<div class=\"amt_val\" id=\"amt" + i + "\" ></div>\n";
	}
	inhtml += "</div>\n";
	inhtml += "<div class=\"slider_div\">\n";
	for (let i = 1 ; i <= num_bins ; i++) {
		inhtml += "\t<div class=\"cell_val\" id=\"cell" + i + "\">\n";
		inhtml += "\t\t<input type=\"range\" name=\"bin" + i + "\" id=\"bin" + i + "\" class=\"form-control slider\" value=\"0\" min=\"0\" max=\"" + tokens + "\" required/>\n";
		inhtml += "\t</div>\n";
	}
	inhtml += "</div>\n";
	inhtml += "<!-- Field for the alternative labels -->\n";
	inhtml += "<input type=\"hidden\" name=\"labelset\" id=\"labelset\" value=0 class=\"form-control\" required />\n";
	inhtml += "<div class=\"submit_div\">\n";
	inhtml += "<div id=\"submit_message\">&nbsp;</div>\n";
	inhtml += "<table id=\"submit_table\"><tr>\n";
	inhtml += "<td style=\"text-align:left;\">\n";

	inhtml += "</td>\n";
	inhtml += "<td style=\"text-align:right;\">\n";
	// We don't show the submit button on the final page
	if (show_submit == 1 & results == 0) {
		let onclick = (results == 0 ? "onclick=\"beliefs_ns.submit_click();\"" : "");
		inhtml += "<button class=\"btn btn-primary btn-large\" type=\"\" id=\"submit_button\" " + onclick + ">INVIA</button>\n";
	}
	inhtml += "</td>\n";
	inhtml += "</tr></table>\n";
	inhtml += "</div>\n";
	inhtml += "</div>\n";
	$("#" + divid).html(inhtml);
}

this.mkview = function(belief_dat, bel_div, results = 0, show_submit = 1) {
	// Make this global to the namespace
	beliefs_ns.belief_dat = belief_dat;
	beliefs_ns.beldat = belief_dat["beldat"];

	let hex_colors = belief_dat["hex_colors"];
	let beldat = belief_dat["beldat"];
	let tokens = belief_dat["tokens"];
	let currency = belief_dat["currency"];
	let num_bins = beldat["num_bins"];
	let labels_selected = 0;

	non_assegnati = tokens;

	// Add the actual stuff to the page
	beliefs_add_content(num_bins, tokens, bel_div, results, show_submit);

	// Fill in some elements from belief_dat
	$("#bar_div").css("border", "1px solid " + hex_colors[0]);
	$(".div_bar").css("background-color", hex_colors[0]);
	$("#round_number").html(belief_dat["round_number"]);
	$("#number_of_rounds").html(belief_dat["number_of_rounds"]);

	if (results == 1) {
		$("#pay_round").html(belief_dat["pay_round"]);
	}

	// First Setup, add the listener functions
	for (let i = 1 ; i <= num_bins; i++ ) {
		let p_left = 100 / num_bins;

		$("#cell" + i).css("bottom", ((i - 1) * 100) + "%");
		$("#cell" + i).css("left", ((i - 1) * p_left) + "%");
		$("#cell" + i).css("width", p_left + "%");

		$("#bar" + i).css("left", ((i - 1) * p_left) + "%");
		$("#bar" + i).css("width", p_left + "%");

		$("#bar_amt" + i).css("left", ((i - 1) * p_left) + "%");
		$("#bar_amt" + i).css("width", p_left + "%");

		$("#amt" + i).css("left", ((i - 1) * p_left) + "%");
		$("#amt" + i).css("width", p_left + "%");
		$("#amt" + i).html(currency + qsr(i));

		$("#prob" + i).css("left", ((i - 1) * p_left) + "%");
		$("#prob" + i).css("width", p_left + "%");
		$("#prob" + i).html(0);

		$("#label" + i).css("left", ((i - 1) * p_left) + "%");
		$("#label" + i).css("width", (p_left - 1) + "%");
		$("#label" + i).css("line-height", "110%");
		$("#label" + i).html(beldat["bin_labels"][i - 1]);

		if (results == 1) {
			$("#bin" + i).val(belief_dat["pay_choices"][i - 1]);
		}

		set_token_allocations(i, beldat)
		$("#bin" + i).on("input change", function() {
			if (results == 1) {
				$("#bin" + i).val(belief_dat["pay_choices"][i - 1]);
			} else {
				set_token_allocations(i, beldat)
			}
		});

		// Log beginning of a slider move
		$("#bin" + i).on("mousedown touchstart", function() {
			log_event('b' + i + '_start_' + 't' + $("#bin" + i).val());
		});

		// Log ending of a slider move
		$("#bin" + i).on("mouseup touchend", function() {
			log_event('b' + i + '_stop_' + 't' + $("#bin" + i).val());
		});
	}

	// listener to log a/href clicks
	$(document).on("click", "a", function(){
		log_event($(this).prop('outerHTML'));
	});

	// Fill the button label based on the label selected initially

	// Fill question text based on the label selected initially
	let question_text = (labels_selected == 0 ? beldat["text"] : beldat["alt_text"]);
	$("#question_div").html(question_text);



	// Set the correct slider position
	$(document).ready(fix_slider_position)
	$(window).resize(fix_slider_position)
	// Set the axis ticks
	axis_stuff(beldat);

	log_event("Start");
}

}
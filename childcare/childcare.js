/*
* Author: Nicholas Hunt-Walker
* 
* Daycare Center Cost Sources:
*
* -- The Seattle Learning Center --
* Site URL: http://seattlelearningcenter.com/enrollment/tuition-schedule/
*   • 12 - 36 months: $1,872 per month
*   • 36 - 60 months: $1,619 - 1,783 per month
*
* -- Little Eagles Child Development Center --
* Site URL: http://www.littleeagles.org/Tuition.html
*   • 1.5 - 15 months: $2,000 per month
*   • 12 - 28 months: $1,900 per month
*   • 21 - 36 months: $1,800 per month
*   • 30 - 72 months: $1,500 per month
*
* -- Tot Spot Kids DayCare --
* Site URL: http://www.tot-spot-kids.com/#!rates-and-services
*   • 0 - 24 months: $300 per week or $1,290 per month (4.3 weeks / month)
*   • 24 - 48 months: $1,290 per month (not potty trained); $250 per week (potty trained) or $\1,075 per month
*   • 48+ months: $1,182.50 per month (not potty trained); $1,075 per month (potty trained)
*
* -- Country Dawn Preschool --
* Site URL: http://www.countrydawnpreschool.com/tuition-rates-2015-2016/
*   • 1 - 12 months: $1,250 per month
*   • 12 - 18 months: $1,080 per month
*   • 18 - 24 months: $995
*   • 24 - 30 months: $995
*   • 30 - 36 months: $995
*   • 3 - 4 years: $930
*   • 4 - 5 years: $950
* 
* -- Creative Sprouts --
* Site URL: http://www.creativesprouts.org/program_info/tuition_info_and_forms
*   • 2 years: $1,407 per month
*   • 3 years: $1,250 per month
*   • 4 years: $1,250
*
* -- Baby Sitter Rates --
* Site URL: https://www.care.com/child-care/seattle-wa
*   • Eyeball averaging $20 per hour or $4,730 per month (11 hrs / day, 5 days / week, 4.3 weeks / month)
*   • Seeing this cost, I don't want to use this in my main calculation, but I might later on for a comparison figure
*/

/* Visualization Phases
* Phase 1.0 - Bare Bones:
* ---------
* Set up a chart showing the cost of daycare per month for one kid. Kid born in
* September 2016, gets out of daycare at age 4. Earliest year is 2015.
* 
* Add rate increases of 4% annually
*
* Add inflation rate (find source)
*
* Add chart totaling accumulated cost for one kid over their time in daycare
* 
* Add chart showing annual cost for one kid over their time in daycare
* 
*
* Phase 2.0 - First variable:
* ---------
* Add variable birthdate with a JS add-on for calendars or written input.
*
*  
* Phase 3.0 - The second kid:
* ---------
* Add a second kid 1.5 years after first
*
* Add a cumulative total line
*
* Make x-axis adjust to total length of time
* 
* Make y-axis adjust to cumulative total line
* 
*
* Phase 4.0 - Variable kids:
* ---------
* Add option to add/remove kids so totals are between 1 and 10 (10?!)
*
* Each new kid gets a name and birthday
*/

// Select and set up basic chart attributes
var margin = {top: 20, right: 5, bottom: 30, left: 70},
    width = 800,
    height = 500,
    chart_width = width - margin.left - margin.right,
    chart_height = height - margin.top - margin.bottom,
    min_cost = 0,
    min_yr = 2015;

// Select chart and set attributes
var chart = d3.select("#figure_container")
        .attr("width", chart_width + margin.left + margin.right)
        .attr("height", chart_height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate("+margin.left+","+margin.top+")");

// Set up x and y scales. x scale is universal. y-scale
// depends on chart in question
var xscale = d3.scale.linear().range([0, chart_width]),
    yscale = d3.scale.linear().range([chart_height, 0]),
    xlabel = "Year",
    ylabel = "Monthly Cost ($1,000)";

// Set up average childcare costs for each age
function mean(data){
    return data.reduce(function(a, b){
        return a + b;
    }) / data.length;
}

var avg_daycare_yr0_1 = mean([2000, 1250, 1290]),
    avg_daycare_yr1_2 = mean([1872, 2000, 1900, 1290, 1250, 1080, 995]),
    avg_daycare_yr2_3 = mean([1872, 1900, 1800, 1290, 1075, 995, 1407]),
    avg_daycare_yr3_4 = mean([1619, 1783, 1500, 1290, 930, 1250]);


// Create a child object
function Child(name, birthday) {
    this.full_name = name;
    var date_arr = new Date(birthday).toString().split(" ");
    this.birthday = new Date(date_arr.slice(0, 2)
                            .concat(date_arr.slice(3)).join(" "));
    this.total_cost = 0;
}

// Plot monthly cost vs. year
function get_age(child, current){
    // return age in n_months
    var birth_yr = child.birthday.getFullYear(),
        birth_month = child.birthday.getMonth(),
        this_yr = current.getFullYear(),
        this_month = current.getMonth(),
        yr_diff = this_yr - birth_yr,
        month_diff = this_month - birth_month,
        age_diff = 0;

    if (child.birthday > current){
        return yr_diff*12 + month_diff;

    } else if (child.birthday === current){
        return 0

    } else {
        return -1

    }
}

function age_check(child, current){
    var age = get_age(child, current);
    if (age > 0){

    } else {
        return false;
    }
}






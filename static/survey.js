document.addEventListener("DOMContentLoaded", function(event) {

            var  president;
            var  congress_party;
            var  congress_1;
            var  congress_2;

            $('li.president').click(function () {
              $(this).toggleClass('selected');
              president=this.id;
              document.getElementById("president").value=president;
              if ($('li.president.selected').length != 0) {
                $('li.president').removeClass('selected');
                $(this).toggleClass('selected');
                president=this.id;
                document.getElementById("president").value=president;
              }
            });

            $('li.congress').click(function () {
              $(this).toggleClass('selected');
              congress_party=this.id;
              document.getElementById("congress_party").value=congress_party;
              document.getElementById("congresista_1_" + congress_party).disabled=false;
              document.getElementById("congresista_2_" + congress_party).disabled=false;
              if ($('li.congress.selected').length != 0) {
                $('li.congress').removeClass('selected');
                $('input[type=number]').attr("disabled",true);
                $(this).toggleClass('selected');
                congress_party=this.id;
                document.getElementById("congress_party").value=congress_party;
                congress_1 = document.getElementById("congresista_1_" + congress_party).disabled=false;
                congress_2 = document.getElementById("congresista_2_" + congress_party).disabled=false;
              }
            });

            $('li.congress1').on('input',function(){
              congress_party = document.querySelector('li.congress.selected').id;
              congress_1 = document.getElementById("congresista_1_" + congress_party).value;
              document.getElementById("congress_1").value=congress_1;
            });

            $('li.congress2').on('input',function(){
              congress_party = document.querySelector('li.congress.selected').id;
              congress_2 = document.getElementById("congresista_2_" + congress_party).value;
              document.getElementById("congress_2").value=congress_2;
            });

 });

$("#formbuttonId").click(function () {

    let Observation = $("#Observation").val();
    let Dsicussion = $("#Dsicussion").val();
    let Conclusion = $("#Conclusion").val();

    var formData = new FormData();

    formData.append('Observation', Observation);
    formData.append('Dsicussion', Dsicussion);
    formData.append('Conclusion', Conclusion);


    $.ajax({
        url: ' https://15f8-103-113-65-59.in.ngrok.io/loadData',
        method: 'POST',
        crossDomain: true,
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {

            alert("Data Store Sucessful !!")


        }
        
    });
    alert("Data Store Sucessful !!")



});


$("#trainmodel").click(function () {

    let Observation = $("#Observation").val();
    let Dsicussion = $("#Dsicussion").val();
    let Conclusion = $("#Conclusion").val();

    var formData = new FormData();

    formData.append('Observation', Observation);
    formData.append('Dsicussion', Dsicussion);
    formData.append('Conclusion', Conclusion);


    $.ajax({
        url: ' https://15f8-103-113-65-59.in.ngrok.io/train_model',
        method: 'POST',
        crossDomain: true,
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {

            alert("Data Store Sucessful !!")

        }
        
    });
    alert("Model Train Sucessfully")

});

$("#trainmodel").click(function () {

    let Observation = $("#Observation").val();
    let Dsicussion = $("#Dsicussion").val();


    var formData = new FormData();

    formData.append('Observation', Observation);
    formData.append('Dsicussion', Dsicussion);
   

    $.ajax({
        url: ' https://15f8-103-113-65-59.in.ngrok.io/test_model',
        method: 'POST',
        crossDomain: true,
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {

            console.log(data)
            var bodtable = '';
            $.each(data, function (index, value) {
                
                console.log(value);
                //bodtable += '<tr data-row=' + value[0] + '><td>' + i + '</td><td data-questionid=' + value[0] + '>' + value[1] + '</td><td style="display:none;">' + value[0] + '</td><td  onclick="gotoNode(' + value[0] + ',`' + value[1] + '`)"> <i class="bi bi-pencil-square"></i></a></td><td  onclick="deleteQuestionAjax(' + value[0] + ',`' + value[1] + '`)"> <i class="bi bi-trash"></i></a></td></tr>';
                bodtable += '<div class="messages__item messages__item--operator">'+ value['question']+'</div>';

            });
            $('#showanser div:last').after(bodtable);
        }
        
    });
    alert("Model Train Sucessfully")

});
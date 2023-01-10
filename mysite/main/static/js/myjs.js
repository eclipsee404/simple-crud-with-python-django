$(document).ready(function () {
  if ($("#result_siswa") != null) {
    read_siswa();
  }

  $("#simpan_siswa").click(function () {
    var data = $("#form_siswa").serialize();

    $.ajax({
      type: "POST",
      url: "siswa_add",
      data: data,
      success: function (data) {
        alert("sukses");
        $("#form_siswa")[0].reset();
        read_siswa();
      },
    });
  });

  $(".edit_siswa").click(function () {
    var id = $(this).attr("name");
    // alert(id);
    $.ajax({
      url: "siswa_read_detail",
      type: "post",
      data: {
        id: id,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: function (response) {
        console.log(response);
        // alert(response.nama_depan.val());
        $("#nama_depan_edit").val(response[0]["fields"]["nama_depan"]);
        $("#nama_belakang_edit").val(response[0]["fields"]["nama_belakang"]);
        $("#siswa_id_edit").val(id);
        var kelas_id = response[0]["fields"]["kelas_id"];
        console.log(kelas_id);
        $("#kelas_id_edit").val(kelas_id).change();
      },
    });
    $("#modal_siswa_edit").modal("toggle");
  });

  $("#update_siswa").click(function () {
    var id = $("#siswa_id_edit").val();
    var data = $("#form_siswa_edit").serialize();
    $.ajax({
      url: "siswa_edit/" + id,
      type: "post",
      data: data,
      success: function (response) {
        alert("sukses");
        $("#form_siswa_edit")[0].reset();
        $("#modal_siswa_edit").modal("hide");
        location.reload();
      },
    });
  });

  $(".delete_siswa").click(function () {
    var id = $(this).attr("name");
    var data = $("#form_siswa_edit").serialize();
    let text;
    if (confirm("Yakin akan delete?") == true) {
      $.ajax({
        url: "siswa_delete/" + id,
        data: data,
        type: "post",
        success: function (response) {
          alert("sukses delete");
          location.reload();
        },
      });
    } else {
      // text = "You canceled!";
    }
  });

  function read_siswa() {
    $.ajax({
      url: "siswa_read",
      type: "post",
      async: false,
      data: {
        res: 1,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: function (response) {
        $("#result_siswa").html(response);
      },
    });
  }
});

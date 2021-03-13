
// editModal
$('#editModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var link_id = button.data('link_id') // Extract information from data-* attributes
        var link_mcg = button.data('link_mcg')
        var link_scg = button.data('link_scg')
        var link_name = button.data('link_name')
        var link_url = button.data('link_url')
        var modal = $(this)
        $("#linkid").attr("action", link_id);
        $("#linkmcg").attr("value", link_mcg);
        $("#linkscg").attr("value", link_scg);
        $("#linkname").attr("value", link_name);
        $("#linkurl").attr("value", link_url);
  })

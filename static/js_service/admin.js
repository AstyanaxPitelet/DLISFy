
const deleteUser = (id) => {
    fetch('/admin/user/delete', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id}),
    }).then((response) => {
        if(response.status === 204) {
            window.location.reload()
        }
    })
}
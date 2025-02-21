function handleUpdate() {
    if (todoText.trim()) {
      db.collection('todos').doc(id).update({
        todoText: todoText,
        completed: completed,
      }).then(() => {
        navigate('/');
      }).catch(function(error) {
        alert('Error updating todo: ' + error.message);
      });
    } else {
      alert('Please enter a todo!');
    }
  }

if (contName.trim()){
db.collection("demo-contacting-app").doc(id).update({
	contName: contName,
	contNos: contNos,
	contMailId: contMailId,
})
.then(() => navigator("/");)
.catch(function(error) {
        alert('Error updating todo: ' + error.message);
      });
    }
else {
      alert('Please enter a todo!');
    }


function handleUpdate(){
	if (contName.trim()){
db.collection("demo-contacting-app").doc(id).update({
	contName: contName,
	contNos: contNos,
	contMailId: contMailId,
})
.then(() => navigator("/");)
.catch(function(error) {
        alert('Error updating todo: ' + error.message);
      });
    }
else {
      alert('Please enter a todo!');
    }
}

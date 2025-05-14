//A javascript code for mobiles example

const initially = {
    noofMobiles: 12
}
function buyMobiles(mobCount) {
    return{
        type: "BUY_MOBILE",
        payload: mobCount
    }
}
const mobileReducer = (state = initially, action) => {
    if (action.type == "BUY_MOBILE") {
        return{
            noofMobiles: state.noofMobiles - action.payload
        }
    }
    return state
}
const mobileStores = reducering.createStore(mobileReducer)
console.log("Firstly", mobileStores.getState())
mobileStores.dispatch(buyMobiles(4))
console.log("Lastly", mobileStores.getState())


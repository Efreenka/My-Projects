import "./OrderButton.css"

const OrderButton = () => {
    const testFunction = () => {
        console.log("Bylo kliknuto")
    }

    return(
        <button type="button" className="btn" onClick={testFunction}>Objednat</button>
    )
}

export default OrderButton

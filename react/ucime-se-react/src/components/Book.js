import "./Book.css"
import OrderButton from "./OrderButton"

const Book = (props) => {
    return (
        <div className="one-book">
            <img src={props.myimage} alt="" />
            <h2 className="main-heading">{props.mytitle}</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit doloremque porro labore. Impedit dolorem reprehenderit dignissimos explicabo beatae laborum vitae quaerat, soluta illum culpa quasi reiciendis aliquid sapiente temporibus earum?</p>
            <OrderButton />
        </div>
    )
}

export default Book

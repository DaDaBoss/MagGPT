import './ButtonEvent.scss';
import type {CSSProperties} from "react";
import {Link} from "react-router-dom";

interface ButtonEventProps {
    image?: string;
    title: string;
    style?: CSSProperties;
    link: string;
}

function ButtonEvent({ image, title, link, style }: ButtonEventProps) {
    return (
        <Link to={link} style={style} className="button_event">
            {image != null ? <img className="button_event__icon" src={image}/> : ``}
            <p className="button_event__title">{title}</p>
        </Link>
    );
}

export default ButtonEvent

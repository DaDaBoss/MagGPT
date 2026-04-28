import './InputChat.scss';
import sendImage from './Assets/send.svg';
import {type CSSProperties, type KeyboardEvent, useState} from "react";

interface InputChatProps {
    placeHolder?: string;
    style?: CSSProperties;
    onSend: (message: string) => void;
}

function InputChat({ placeHolder, style, onSend }: InputChatProps) {


    const [value, setValue] = useState("");

    const send = () => {
        const text = value.trim();
        if (!text) return;

        onSend(text);
        setValue("");
    };

    const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            send();
        }
    };

    return (
        <div
            style={style}
            className={`input_chat`}>
            <textarea
                className={'input_chat__input'}
                onKeyDown={handleKeyDown}
                onChange={(e) => setValue(e.target.value)}
                value={value}
                placeholder={placeHolder}
            />
            <button type="submit"
                    onClick={send}
                    className={'input_chat__send_button'}>
                <img src={sendImage}/>
            </button>
        </div>
    );
}

export default InputChat;
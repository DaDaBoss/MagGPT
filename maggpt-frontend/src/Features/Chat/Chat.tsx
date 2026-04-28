import './Chat.scss'
import InputChat from "../../Shared/InputChat/InputChat.tsx";
import {useEffect, useRef, useState} from "react";
import Message from "./Models/Message.ts";
import {useParams} from "react-router-dom";


function Chat()  {
    const { id } = useParams();
    const [messages, setMessages] = useState<Message[]>([]);
    const messagesEndRef = useRef<HTMLDivElement | null>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSendMessage = (text: string) => {
        if (!text.trim()) return;

        setMessages(prev => [
            ...prev,
            new Message(text, "user")
        ]);
    };

    function GetChatMessages() {

        if (id !== undefined) {
            return <form className="chat chat__started">
                <div className="chat__messages">

                    <div>
                        {messages.map((m) => (
                            <div className={`message ${m.sender == 'user' ? 'message__user' : 'message__system'}`}>
                                {m.text}
                            </div>
                        ))}
                    </div>
                    <div ref={messagesEndRef} />
                </div>
                <InputChat
                    onSend={handleSendMessage}
                    placeHolder={'Введите свой вопрос...'}/>
            </form>
        }

        return (
            <form className="chat">
                <h2 className='chat__title'>Спросите у MagGPT</h2>
                <InputChat onSend={handleSendMessage} placeHolder={'Введите свой вопрос...'}/>
            </form>
        );
    }

    return (
        GetChatMessages()
    );
}

export default Chat

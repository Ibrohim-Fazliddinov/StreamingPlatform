import styles from './ButtonGradient.module.css';

export default function ButtonGradient({ icon, text, isAnimationIcon }) {
    return (
        <button className={styles.wrapper}>
            <span>{text}</span>
            {icon ? (
                <span
                    className={
                        isAnimationIcon
                            ? `${styles.icon} ${styles.animationIcon}`
                            : styles.icon
                    }
                >
                    {icon}
                </span>
            ) : null}
        </button>
    );
}

import styles from './MainProgressBar.module.css';

export default function MainProgressBar({ value }) {
    return (
        <div className={styles.progressWrapper}>
            <div className={styles.currProgressState}>{value}</div>
            <progress
                value={value}
                max="4"
                className={styles.progress}
            ></progress>
            <div className={styles.nextProgressState}>{value + 1}</div>
        </div>
    );
}

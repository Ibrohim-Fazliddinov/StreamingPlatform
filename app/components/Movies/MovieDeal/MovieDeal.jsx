import styles from './MovieDeal.module.css';

export default function MovieDeal() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.preview}></div>
            <div className={styles.title}>Love and War</div>
        </div>
    );
}

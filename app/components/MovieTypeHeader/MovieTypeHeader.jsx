import styles from './MovieTypeHeader.module.css';

export default function MovieTypeHeader() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.left}>
                <h2 className={styles.title}>Deal of the Week</h2>
                <h3 className={styles.descr}>
                    Celebrity interviews, trending entertainment stories, and
                    expert analysis
                </h3>
            </div>
            <div className={styles.right}>
                <div className={styles.rightText}>View all</div>
                <div className={styles.arrow}>&gt;</div>
            </div>
        </div>
    );
}

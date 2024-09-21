'use client';
import { Swiper, SwiperSlide } from 'swiper/react';
import {
    FreeMode,
    Navigation,
    Thumbs,
    Pagination,
    Autoplay,
} from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/free-mode';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/thumbs';

import styles from './page.module.css';
import Container from './components/Container/Container';
import { useRef, useState } from 'react';
import MainPreviewContent from './components/MainPreviewContent/MainPreviewContnent';
import MainProgressBar from './components/MainProgressBar/MainProgressBar';
import MovieTypeHeader from './components/MovieTypeHeader/MovieTypeHeader';
import ButtonGradient from './components/UI/ButtonGradient/ButtonGradient';
import PlayIcon from '/public/icons/play.svg';
import MovieDeal from './components/Movies/MovieDeal/MovieDeal';
import MovieRelease from './components/Movies/MovieRelease/MovieRelease';
import MovieTrend from './components/Movies/MovieTrend/MovieTrend';
import MovieRecommended from './components/Movies/MovieRecommended/MovieRecommended';
import MovieExclusive from './components/Movies/MovieExclusive/MovieExclusive';
export default function Homepage() {
    const mainSwiperRef = useRef();
    const [currMainPreviewNum, setCurrMainPreviewNum] = useState(1);
    const [thumbsSwiper, setThumbsSwiper] = useState(null);
    console.log(thumbsSwiper);
    return (
        <>
            <section className={styles.mainSection}>
                <div className={styles.swiperWrapper}>
                    <Swiper
                        onSlideChange={(e) => {
                            setCurrMainPreviewNum(e.activeIndex + 1 || 1);
                        }}
                        className={styles.mainSwiper}
                        onSwiper={(swiper) => (mainSwiperRef.current = swiper)}
                    >
                        <SwiperSlide>
                            <div
                                style={{ background: 'red' }}
                                className={styles.swiperSlide}
                            >
                                <MainPreviewContent />
                            </div>
                        </SwiperSlide>
                        <SwiperSlide>
                            <div
                                style={{ background: 'orange' }}
                                className={styles.swiperSlide}
                            >
                                {' '}
                                <MainPreviewContent />
                            </div>
                        </SwiperSlide>
                        <SwiperSlide>
                            <div
                                style={{ background: 'black' }}
                                className={styles.swiperSlide}
                            >
                                <MainPreviewContent />
                            </div>
                        </SwiperSlide>
                        <SwiperSlide>
                            <div
                                style={{ background: 'white' }}
                                className={styles.swiperSlide}
                            >
                                {' '}
                                <MainPreviewContent />
                            </div>
                        </SwiperSlide>
                        <SwiperSlide>
                            <div
                                style={{ background: 'purple' }}
                                className={styles.swiperSlide}
                            >
                                {' '}
                                <MainPreviewContent />
                            </div>
                        </SwiperSlide>

                        <MainProgressBar value={currMainPreviewNum} />
                    </Swiper>
                </div>
                <button
                    onClick={() => mainSwiperRef.current.slidePrev()}
                    className={`${styles.mainArrowWrapper} ${styles.mainArrowLeft}`}
                >
                    <div className={`${styles.mainArrow}`}>&lt;</div>
                </button>
                <button
                    onClick={() => mainSwiperRef.current.slideNext()}
                    className={`${styles.mainArrowWrapper} ${styles.mainArrowRight}`}
                >
                    <div className={`${styles.mainArrow}`}>&gt;</div>
                </button>
            </section>
            <section className={styles.trendingMovies}>
                <Container>
                    <MovieTypeHeader />
                    <Swiper
                        slidesPerView={'auto'}
                        centeredSlides={false}
                        spaceBetween={16}
                        grabCursor={true}
                        pagination={{
                            clickable: true,
                        }}
                        modules={[Pagination]}
                        className={styles.trendingMoviesSwiper}
                    >
                        {Array.from({ length: 10 }, () => null).map((i) => (
                            <SwiperSlide key={Math.random()}>
                                <MovieTrend />
                            </SwiperSlide>
                        ))}
                    </Swiper>
                </Container>
            </section>
            <section className={styles.newRelease}>
                <Container>
                    <MovieTypeHeader />
                    <Swiper
                        slidesPerView={'auto'}
                        grabCursor={true}
                        spaceBetween={16}
                        className={styles.releaseSwiper}
                    >
                        {Array.from({ length: 10 }, () => null).map((i) => (
                            <SwiperSlide key={Math.random()}>
                                <MovieRelease />
                            </SwiperSlide>
                        ))}
                    </Swiper>
                </Container>
            </section>
            <section className={styles.almostAdults}>
                <Container>
                    <div className={styles.almostAdultsWrapper}>
                        <div className={styles.almostAdultsLeft}>
                            <div className={styles.almostAdultsTitle}>
                                Almost Adults
                            </div>
                            <div className={styles.almostAdultsDescr}>
                                This comedy feature follows two best friends in
                                their final year of college while they
                                transition into adulthood. One embraces her
                                sexuality and….
                            </div>
                            <div className={styles.almostAdultsDetails}>
                                <ButtonGradient
                                    text={'Play Now'}
                                    icon={<PlayIcon />}
                                    isAnimationIcon={true}
                                />
                                <button className={styles.almostAdultsBtnPlus}>
                                    <div
                                        className={styles.almostAdultsPlusLine}
                                    ></div>
                                    <div
                                        className={styles.almostAdultsPlusLine}
                                    ></div>
                                </button>
                            </div>
                        </div>
                        <div className={styles.almostAdultsRight}>
                            <div className={styles.almostAdultsSwiperWrapper}>
                                {' '}
                                <Swiper
                                    loop={true}
                                    spaceBetween={10}
                                    navigation={false}
                                    thumbs={{ swiper: thumbsSwiper }}
                                    modules={[FreeMode, Navigation, Thumbs]}
                                    className={styles.almostAdultsSwiper}
                                >
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'red',
                                            }}
                                            className={
                                                styles.almostAdultsSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'blue',
                                            }}
                                            className={
                                                styles.almostAdultsSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'orange',
                                            }}
                                            className={
                                                styles.almostAdultsSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'black',
                                            }}
                                            className={
                                                styles.almostAdultsSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'purple',
                                            }}
                                            className={
                                                styles.almostAdultsSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'aqua',
                                            }}
                                            className={
                                                styles.almostAdultsSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                </Swiper>
                                <Swiper
                                    onSwiper={setThumbsSwiper}
                                    direction={'vertical'}
                                    loop={true}
                                    spaceBetween={16}
                                    slidesPerView={4}
                                    freeMode={true}
                                    watchSlidesProgress={true}
                                    modules={[FreeMode, Navigation, Thumbs]}
                                    className={styles.almostAdultsSecondSwiper}
                                >
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'red',
                                            }}
                                            className={
                                                styles.almostAdultsSecondSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'blue',
                                            }}
                                            className={
                                                styles.almostAdultsSecondSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'orange',
                                            }}
                                            className={
                                                styles.almostAdultsSecondSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'black',
                                            }}
                                            className={
                                                styles.almostAdultsSecondSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'purple',
                                            }}
                                            className={
                                                styles.almostAdultsSecondSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                    <SwiperSlide>
                                        <div
                                            style={{
                                                background: 'aqua',
                                            }}
                                            className={
                                                styles.almostAdultsSecondSwiperItem
                                            }
                                        ></div>
                                    </SwiperSlide>
                                </Swiper>
                            </div>
                        </div>
                    </div>
                </Container>
            </section>
            <section className={styles.dealOfTheWeek}>
                <Container>
                    <MovieTypeHeader />
                    <Swiper
                        slidesPerView={'auto'}
                        grabCursor={true}
                        spaceBetween={16}
                        className={styles.dealSwiper}
                    >
                        {Array.from({ length: 10 }, () => null).map((i) => (
                            <SwiperSlide key={Math.random()}>
                                <MovieDeal />
                            </SwiperSlide>
                        ))}
                    </Swiper>
                </Container>
            </section>
            <section className={styles.tvSeries}>
                <Container>
                    {' '}
                    <div className={styles.tvSeriesDescr}>
                        <div className={styles.tvSeriesDescrLeft}>
                            TV Series
                        </div>
                        <div className={styles.tvSeriesDescrRight}>
                            <div className={styles.tvSeriesDates}>
                                <div className={styles.tvSeriesDateItem}>
                                    Today
                                </div>
                                <div className={styles.tvSeriesDateItem}>
                                    This week
                                </div>
                                <div className={styles.tvSeriesDateItem}>
                                    This month
                                </div>
                                <div className={styles.tvSeriesDateItem}>
                                    Last 3 month
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={styles.tvSeriesGrid}>
                        <div className={styles.tvSeriesGridItem}>
                            <div className={styles.tvSeriesText}>
                                <div className={styles.tvSeriesTitle}>
                                    Falling Water
                                </div>
                                <div className={styles.seasons}>2 Seasons</div>
                            </div>
                        </div>
                        <div className={styles.tvSeriesGridItem}>
                            <div className={styles.tvSeriesText}>
                                <div className={styles.tvSeriesTitle}>
                                    Falling Water
                                </div>
                                <div className={styles.tvSeriesSeason}>
                                    2 Seasons
                                </div>
                            </div>
                        </div>{' '}
                        <div className={styles.tvSeriesGridItem}>
                            <div className={styles.tvSeriesText}>
                                <div className={styles.tvSeriesTitle}>
                                    Falling Water
                                </div>
                                <div className={styles.tvSeriesSeason}>
                                    2 Seasons
                                </div>
                            </div>
                        </div>{' '}
                        <div className={styles.tvSeriesGridItem}>
                            <div className={styles.tvSeriesText}>
                                <div className={styles.tvSeriesTitle}>
                                    Falling Water
                                </div>
                                <div className={styles.tvSeriesSeason}>
                                    2 Seasons
                                </div>
                            </div>
                        </div>{' '}
                        <div className={styles.tvSeriesGridItem}>
                            <div className={styles.tvSeriesText}>
                                <div className={styles.tvSeriesTitle}>
                                    Falling Water
                                </div>
                                <div className={styles.tvSeriesSeason}>
                                    2 Seasons
                                </div>
                            </div>
                        </div>{' '}
                        <div className={styles.tvSeriesGridItem}>
                            <div className={styles.tvSeriesText}>
                                <div className={styles.tvSeriesTitle}>
                                    Falling Water
                                </div>
                                <div className={styles.tvSeriesSeason}>
                                    2 Seasons
                                </div>
                            </div>
                        </div>{' '}
                        <div className={styles.tvSeriesGridItem}>
                            <div className={styles.tvSeriesText}>
                                <div className={styles.tvSeriesTitle}>
                                    Falling Water
                                </div>
                                <div className={styles.tvSeriesSeason}>
                                    2 Seasons
                                </div>
                            </div>
                        </div>
                    </div>
                </Container>
            </section>
            <section className={styles.recommended}>
                <Container>
                    <MovieTypeHeader />
                    <Swiper
                        slidesPerView={'auto'}
                        loop={true}
                        grabCursor={true}
                        spaceBetween={16}
                        autoplay={{
                            delay: 5000,
                            disableOnInteraction: false,
                        }}
                        modules={[Autoplay, Pagination, Navigation]}
                        className={styles.recommendedSwiper}
                    >
                        {Array.from({ length: 10 }, () => null).map((i) => (
                            <SwiperSlide key={Math.random()}>
                                <MovieRecommended />
                            </SwiperSlide>
                        ))}
                    </Swiper>
                </Container>
            </section>
            <section className={styles.exclusive}>
                <Container>
                    <MovieTypeHeader />
                    <Swiper
                        slidesPerView={'auto'}
                        spaceBetween={16}
                        modules={[Pagination]}
                        className={styles.exclusiveSwiper}
                    >
                        <SwiperSlide>
                            <MovieExclusive />
                        </SwiperSlide>
                        <SwiperSlide>
                            <MovieExclusive />
                        </SwiperSlide>
                        <SwiperSlide>
                            <MovieExclusive />
                        </SwiperSlide>
                    </Swiper>
                </Container>
            </section>
        </>
    );
}

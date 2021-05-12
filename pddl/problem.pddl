(define(problem satprob)
(:domain SimpleSatellite)
(:objects
  mem0 mem1 mem2 mem3 mem4 mem5 mem6 mem7 mem8 mem9 - memory
 img0 img1 img2 img3 img4 img5 img6 img7 img8 img9 - image
)
(:init
  (sat_free)
  (= (total_score) 0)

  (memory_free mem0)
  (memory_free mem1)
  (memory_free mem2)
  (memory_free mem3)
  (memory_free mem4)
  (memory_free mem5)
  (memory_free mem6)
  (memory_free mem7)
  (memory_free mem8)
  (memory_free mem9)

  (at 436.595 (image_available img0))
  (at 441.595 (not (image_available img0)))
  (at 576.458 (image_available img1))
  (at 581.458 (not (image_available img1)))
  (at 252.804 (image_available img2))
  (at 257.804 (not (image_available img2)))
  (at 127.863 (image_available img3))
  (at 132.863 (not (image_available img3)))
  (at 458.913 (image_available img4))
  (at 463.913 (not (image_available img4)))
  (at 424.568 (image_available img5))
  (at 429.568 (not (image_available img5)))
  (at 353.698 (image_available img6))
  (at 358.698 (not (image_available img6)))
  (at 2.92 (image_available img7))
  (at 7.92 (not (image_available img7)))
  (at 178.953 (image_available img8))
  (at 183.953 (not (image_available img8)))
  (at 531.213 (image_available img9))
  (at 536.213 (not (image_available img9)))
  (at 1036.595 (image_available img0))
  (at 1041.595 (not (image_available img0)))
  (at 1176.458 (image_available img1))
  (at 1181.458 (not (image_available img1)))
  (at 852.804 (image_available img2))
  (at 857.804 (not (image_available img2)))
  (at 727.863 (image_available img3))
  (at 732.863 (not (image_available img3)))
  (at 1058.913 (image_available img4))
  (at 1063.913 (not (image_available img4)))
  (at 1024.568 (image_available img5))
  (at 1029.568 (not (image_available img5)))
  (at 953.698 (image_available img6))
  (at 958.698 (not (image_available img6)))
  (at 602.92 (image_available img7))
  (at 607.92 (not (image_available img7)))
  (at 778.953 (image_available img8))
  (at 783.953 (not (image_available img8)))
  (at 1131.213 (image_available img9))
  (at 1136.213 (not (image_available img9)))
  (at 1636.595 (image_available img0))
  (at 1641.595 (not (image_available img0)))
  (at 1776.458 (image_available img1))
  (at 1781.458 (not (image_available img1)))
  (at 1452.804 (image_available img2))
  (at 1457.804 (not (image_available img2)))
  (at 1327.863 (image_available img3))
  (at 1332.863 (not (image_available img3)))
  (at 1658.913 (image_available img4))
  (at 1663.913 (not (image_available img4)))
  (at 1624.568 (image_available img5))
  (at 1629.568 (not (image_available img5)))
  (at 1553.698 (image_available img6))
  (at 1558.698 (not (image_available img6)))
  (at 1202.92 (image_available img7))
  (at 1207.92 (not (image_available img7)))
  (at 1378.953 (image_available img8))
  (at 1383.953 (not (image_available img8)))
  (at 1731.213 (image_available img9))
  (at 1736.213 (not (image_available img9)))
  (at 2236.595 (image_available img0))
  (at 2241.595 (not (image_available img0)))
  (at 2376.458 (image_available img1))
  (at 2381.458 (not (image_available img1)))
  (at 2052.804 (image_available img2))
  (at 2057.804 (not (image_available img2)))
  (at 1927.863 (image_available img3))
  (at 1932.863 (not (image_available img3)))
  (at 2258.913 (image_available img4))
  (at 2263.913 (not (image_available img4)))
  (at 2224.568 (image_available img5))
  (at 2229.568 (not (image_available img5)))
  (at 2153.698 (image_available img6))
  (at 2158.698 (not (image_available img6)))
  (at 1802.92 (image_available img7))
  (at 1807.92 (not (image_available img7)))
  (at 1978.953 (image_available img8))
  (at 1983.953 (not (image_available img8)))
  (at 2331.213 (image_available img9))
  (at 2336.213 (not (image_available img9)))
  (at 2836.595 (image_available img0))
  (at 2841.595 (not (image_available img0)))
  (at 2976.458 (image_available img1))
  (at 2981.458 (not (image_available img1)))
  (at 2652.804 (image_available img2))
  (at 2657.804 (not (image_available img2)))
  (at 2527.863 (image_available img3))
  (at 2532.863 (not (image_available img3)))
  (at 2858.913 (image_available img4))
  (at 2863.913 (not (image_available img4)))
  (at 2824.568 (image_available img5))
  (at 2829.568 (not (image_available img5)))
  (at 2753.698 (image_available img6))
  (at 2758.698 (not (image_available img6)))
  (at 2402.92 (image_available img7))
  (at 2407.92 (not (image_available img7)))
  (at 2578.953 (image_available img8))
  (at 2583.953 (not (image_available img8)))
  (at 2931.213 (image_available img9))
  (at 2936.213 (not (image_available img9)))

  (at 271.99 (dump_available))
  (at 321.99 (not (dump_available)))
  (at 871.99 (dump_available))
  (at 921.99 (not (dump_available)))
  (at 1471.99 (dump_available))
  (at 1521.99 (not (dump_available)))
  (at 2071.99 (dump_available))
  (at 2121.99 (not (dump_available)))
  (at 2671.99 (dump_available))
  (at 2721.99 (not (dump_available)))
)
(:goal (and
  (image_dumped img0)
  (image_dumped img1)
  (image_dumped img2)
)))
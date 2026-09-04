// React Theme — extracted from https://www.monologue.to/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
    neutral900: string;
 *   };
 *   fonts: {
    mono: string;
    body: string;
 *   };
 *   fontSizes: {
    '24': string;
    '26': string;
    '28': string;
    '32': string;
    '46': string;
    '48': string;
    '52': string;
    '72': string;
    '92': string;
    '46.44': string;
    '38.095': string;
    '22.291': string;
 *   };
 *   space: {
    '1': string;
    '19': string;
    '26': string;
    '31': string;
    '35': string;
    '40': string;
    '47': string;
    '50': string;
    '52': string;
    '58': string;
    '60': string;
    '64': string;
    '66': string;
    '72': string;
    '75': string;
    '80': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    xs: string;
    sm: string;
    md: string;
    lg: string;
    xl: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#ef8a80",
    "secondary": "#dcca65",
    "accent": "#326ec8",
    "background": "#121212",
    "foreground": "#ffffff",
    "neutral50": "#f2f0ed",
    "neutral100": "#ffffff",
    "neutral200": "#111111",
    "neutral300": "#272727",
    "neutral400": "#000000",
    "neutral500": "#343434",
    "neutral600": "#1b1b1b",
    "neutral700": "#909090",
    "neutral800": "#777777",
    "neutral900": "#b2b2b2"
  },
  "fonts": {
    "mono": "'monologueSerifItalic', monospace",
    "body": "'instrumentSerifItalic', sans-serif"
  },
  "fontSizes": {
    "24": "24px",
    "26": "26px",
    "28": "28px",
    "32": "32px",
    "46": "46px",
    "48": "48px",
    "52": "52px",
    "72": "72px",
    "92": "92px",
    "46.44": "46.44px",
    "38.095": "38.095px",
    "22.291": "22.291px"
  },
  "space": {
    "1": "1px",
    "19": "19px",
    "26": "26px",
    "31": "31px",
    "35": "35px",
    "40": "40px",
    "47": "47px",
    "50": "50px",
    "52": "52px",
    "58": "58px",
    "60": "60px",
    "64": "64px",
    "66": "66px",
    "72": "72px",
    "75": "75px",
    "80": "80px"
  },
  "radii": {
    "xs": "1px",
    "sm": "4px",
    "md": "10px",
    "lg": "14px",
    "xl": "22px",
    "full": "999px"
  },
  "shadows": {
    "xs": "rgba(255, 255, 255, 0.25) -1px 0px 1px 0px, rgba(255, 255, 255, 0.25) 1px 0px 1px 0px, rgba(255, 255, 255, 0.25) 0px -1px 0.5px 0px inset",
    "sm": "rgba(0, 0, 0, 0.1) 0px 1px 4px 0px",
    "md": "rgba(0, 0, 0, 0.19) 0px 4px 8px 0px, rgba(0, 0, 0, 0.17) 0px 15px 15px 0px, rgba(0, 0, 0, 0.1) 0px 34px 20px 0px, rgba(0, 0, 0, 0.03) 0px 60px 24px 0px",
    "lg": "rgba(0, 0, 0, 0.42) 0px 12px 18px 0px",
    "xl": "rgba(0, 0, 0, 0.04) 0px 208px 83px 0px, rgba(0, 0, 0, 0.14) 0px 117px 70px 0px, rgba(0, 0, 0, 0.23) 0px 52px 52px 0px, rgba(0, 0, 0, 0.27) 0px 13px 29px 0px"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#ef8a80",
      "light": "hsl(5, 78%, 87%)",
      "dark": "hsl(5, 78%, 57%)"
    },
    "secondary": {
      "main": "#dcca65",
      "light": "hsl(51, 63%, 78%)",
      "dark": "hsl(51, 63%, 48%)"
    },
    "background": {
      "default": "#121212",
      "paper": "#272727"
    },
    "text": {
      "primary": "#ffffff",
      "secondary": "#f2f0ed"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "46px",
      "fontWeight": "400",
      "lineHeight": "46px"
    }
  },
  "shape": {
    "borderRadius": 7
  },
  "shadows": [
    "rgba(0, 0, 0, 0.6) 0px 0px 0.25px 0px",
    "rgba(0, 0, 0, 0.16) 0px 0.184px 0.184px 0px, rgba(0, 0, 0, 0.25) 0px 0.092px 5.517px 0px, rgba(255, 255, 255, 0.2) 0px 0.276px 0.276px 0px inset, rgba(0, 0, 0, 0.16) 0px -0.276px 0.552px 0px inset",
    "rgba(255, 255, 255, 0.1) 0px 0px 0.416667px 0.833333px",
    "rgba(0, 0, 0, 0.6) 0px 0px 0.5px 1px",
    "rgba(255, 255, 255, 0.1) 0px 0px 0.5px 1px"
  ]
};

export default theme;
